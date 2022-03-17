from pathlib import Path
import sys

from storage.model.config import AppConfig
from storage.service.redis import RedisService

from loguru import logger


def run(config_path: Path):
    with open(config_path, "r") as f:
        config = AppConfig.from_json(f.read())
    
    redis_service = RedisService(config.redis_config)

    logger.info(f"Listening for messages in Redis queue '{config.redis_config.queue}'.")
    while True:
        measurement = redis_service.receive()


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        logger.error("Usage: python main.py CONFIG_FILE_PATH")
        sys.exit(1)
    else:
        run(Path(args[0]))