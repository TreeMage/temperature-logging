from functools import lru_cache
import os
from pathlib import Path

from fastapi import Depends

from api.model.config import AppConfig, StorageConfig
from api.serivce.repository import MeasurementRepository, StatisticsRepository
from api.serivce.storage import StorageService

CONFIG_VAR="CONF"

@lru_cache
def get_config():
    #path = os.environ.get(CONFIG_VAR)
    #with open(path, "r") as f:
    #    config = AppConfig.from_json(f.read())
    #return config
    return AppConfig(StorageConfig("/tmp/storage.db", "measurements"))


@lru_cache
def get_storage_service(config: AppConfig = Depends(get_config)):
    return StorageService(config.storage_config)


@lru_cache
def get_statistics_repository(storage_service: StorageService = Depends(get_storage_service)):
    return StatisticsRepository(storage_service)


@lru_cache
def get_measurement_repository(storage_service: StorageService = Depends(get_storage_service)):
    return MeasurementRepository(storage_service)