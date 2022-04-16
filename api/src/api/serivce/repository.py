from typing import List
from api.model.measurement import Measurement
from api.serivce.storage import StorageService
from datetime import datetime


class StatisticsRepository:
    def __init__(self, storage_service: StorageService) -> None:
        self._storage = storage_service
    

    def count(self) -> int:
        query = "SELECT COUNT(*) FROM {};"
        results = self._storage.execute_select(query)
        return results[0][0]

    def count_between(self, start: datetime, end: datetime) -> int:
        query = "SELECT COUNT(*) FROM {} WHERE timestamp BETWEEN ? AND ?;"
        results = self._storage.execute_select(
            query=query,
            query_params=(datetime.timestamp(start), datetime.timestamp(end))
        )
        return results[0][0]


class MeasurementRepository:
    def __init__(self, storage_service: StorageService) -> None:
        self._storage = storage_service
    
    def by_id(self, measurement_id: int) -> Measurement:
        query = "SELECT temperature, humidity, timestamp FROM {} where id = ?"
        results = self._storage.execute_select(
            query=query,
            query_params=(measurement_id,)
            )
        temperature, humidity, timestamp = results[0]
        return Measurement(
            temperature=temperature,
            humidity=humidity,
            timestamp=datetime.fromtimestamp(timestamp)
        )

    def between(self, start: datetime, end: datetime) -> List[Measurement]:
        query = "SELECT temperature, humidity, timestamp FROM {} WHERE timestamp between ? AND ? ORDER BY timestamp ASC;"
        results = self._storage.execute_select(
            query=query,
            query_params=(datetime.timestamp(start), datetime.timestamp(end))
        )
        return list(
            map(lambda r: Measurement(
                temperature=r[0],
                humidity=r[1],
                timestamp=datetime.fromtimestamp(r[2])
            ), results)
        )
