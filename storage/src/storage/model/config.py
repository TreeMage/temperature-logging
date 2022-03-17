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
class DatabaseConfig:
    path: str
    table: str


@dataclass_json
@dataclass
class AppConfig:
    measurement_buffer: int
    redis_config: RedisConfig
    database_config: DatabaseConfig