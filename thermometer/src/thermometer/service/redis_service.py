import redis
from thermometer.model.config import RedisConfig
from thermometer.model.measurement import Measurement


class RedisService:
    def __init__(self, config: RedisConfig) -> None:
        self.config = config
        self._client = redis.Redis(
            host=config.host,
            port=config.port,
            db=config.db
        )
    
    def send(self, measurement: Measurement) -> None:
        serialized = Measurement.to_json(measurement)
        self._client.lpush(self.config.queue, serialized)
