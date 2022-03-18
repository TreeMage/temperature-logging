from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass(frozen=True)
class RedisConfig:
    host: str
    port: int
    queue: str
    db: int
    charset: str


@dataclass_json
@dataclass(frozen=True)
class StorageConfig:
    path: str
    table: str


@dataclass_json
@dataclass
class AppConfig:
    buffer_size: int
    redis_retry_interval: int
    redis_config: RedisConfig
    storage_config: StorageConfig