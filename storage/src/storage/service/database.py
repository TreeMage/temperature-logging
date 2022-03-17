import sqlite3
from typing import List
from storage.model.config import DatabaseConfig
from storage.model.measurement import Measurement


class StorageService:
    def __init__(self, config: DatabaseConfig) -> None:
        self.config = config
        self._connection = sqlite3.connect(config.path)
    

    def setup(self) -> None:
        cur = self._connection.cursor()
        cur.execute(f"""CREATE TABLE {self.config.table} IF NOT EXISTS 
        (id integer primary key, temperature float, humidity float, timestamp datetime);""")
        cur.execute(f"CREATE INDEX IF NOT EXISTS time_index ON {self.config.table} (timestamp)")
        cur.close()

    def save(self, measurements: List[Measurement]) -> None:
        query = f"INSERT INTO {self.config.table} VALUES (null, ?, ? ,?);"
        cur = self._connection.cursor()
        cur.executemany(
            query,
            map(lambda m: (m.temperature, m.humidity, m.timestamp), measurements)
        )
        cur.close()