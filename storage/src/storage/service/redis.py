import redis
from storage.model.config import RedisConfig
from storage.model.measurement import Measurement


class RedisService:
    def __init__(self, config: RedisConfig) -> None:
        self.config = config
        self._client = redis.Redis(
            host=config.host,
            port=config.port,
            db=config.db
        )
    
    def receive(self) -> Measurement:
        _, data = self._client.brpop(self.config.queue)
        serialized = data.decode(self.config.charset)
        return Measurement.from_json(serialized) 