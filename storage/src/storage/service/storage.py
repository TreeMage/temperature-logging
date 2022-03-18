import sqlite3
from typing import List
from storage.model.config import StorageConfig
from storage.model.measurement import Measurement


class StorageService:
    def __init__(self, config: StorageConfig) -> None:
        self.config = config
        self._connection = sqlite3.connect(config.path)
    

    def setup(self) -> None:
        cur = self._connection.cursor()
        cur.execute(f"""CREATE TABLE IF NOT EXISTS {self.config.table} (id integer primary key, temperature float, humidity float, timestamp timestamp);""")
        cur.execute(f"CREATE INDEX IF NOT EXISTS time_index ON {self.config.table} (timestamp)")
        cur.close()
        self._connection.commit()

    def save(self, measurements: List[Measurement]) -> None:
        query = f"INSERT INTO {self.config.table} VALUES (null, ?, ? ,?);"
        cur = self._connection.cursor()
        values = list(map(lambda m: (m.temperature, m.humidity, m.timestamp.timestamp()), measurements))
        cur.executemany(
            query,
            values
        )
        cur.close()
        self._connection.commit()