from pathlib import Path
import sys
import time

from storage.model.config import AppConfig
from storage.service.storage import StorageService
from storage.service.redis import RedisService

from loguru import logger


def run(config_path: Path):
    with open(config_path, "r") as f:
        config = AppConfig.from_json(f.read())
    
    storage_service = StorageService(config.storage_config)
    redis_service = RedisService(config.redis_config)

    logger.info("Initializing database.")
    storage_service.setup()

    logger.info(f"Listening for messages in Redis queue '{config.redis_config.queue}'.")
    buffer = []
    while True:
        try:
            measurement = redis_service.receive()
        except Exception as e:
            logger.error(f"Failed to retrieve record from redis. Retrying in {config.redis_retry_interval}s.")
            time.sleep(config.redis_retry_interval)
            continue

        buffer.append(measurement)
        if len(buffer) >= config.buffer_size:
            logger.info(f"Storing {len(buffer)} measurements.")
            storage_service.save(buffer)
            buffer.clear()


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        logger.error("Usage: python main.py CONFIG_FILE_PATH")
        sys.exit(1)
    else:
        run(Path(args[0]))