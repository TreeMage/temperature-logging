from pathlib import Path
import sys
import time

from thermometer.model.config import AppConfig
from thermometer.service.measurement_service import MeasurementService
from thermometer.service.redis_service import RedisService

from loguru import logger


def run(config_path: Path):
    with open(config_path, "r") as f:
        config = AppConfig.from_json(f.read())
    
    interval = config.measurement_config.interval

    redis_service = RedisService(config.redis_config)
    measurement_service = MeasurementService()

    while True:
        measurement = measurement_service.measure()
        try:
            redis_service.send(measurement)
        except Exception as e:
            logger.error(f"Failed to publish measurement to Redis: {e}")
        time.sleep(interval)

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        logger.error("Usage: python main.py CONFIG_FILE_PATH")
        sys.exit(1)
    else:
        run(Path(args[0]))