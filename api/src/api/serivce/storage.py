from typing import Iterable, Optional
from api.model.config import StorageConfig
import sqlite3

class StorageService:
    def __init__(self, config: StorageConfig) -> None:
        self.config = config

    def execute_select(self, query: str, query_params = None) -> list:
        formatted_query = query.format(self.config.table)
        if query_params is None:
            query_params = []
        with sqlite3.connect(self.config.path) as con:
            cur = con.cursor()
            result =  cur.execute(formatted_query, query_params).fetchall()
            cur.close()
        return result


    

    