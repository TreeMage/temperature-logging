from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(frozen=True)
class RedisConfig:
    host: str
    port: int
    queue: str
    db: int

@dataclass_json
@dataclass(frozen=True)
class MeasurementConfig:
    num_measurements: int
    pin: str


@dataclass_json
@dataclass(frozen=True)
class AppConfig:
    measurement_delay: int
    measurement_config: MeasurementConfig
    redis_config: RedisConfig
