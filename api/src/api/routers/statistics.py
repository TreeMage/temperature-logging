from datetime import datetime
from fastapi import Depends, APIRouter

from api.serivce.repository import StatisticsRepository

from api.dependencies import get_statistics_repository

router = APIRouter(
    prefix="/stats",
    tags=["statistics"],
)

@router.get("/count")
async def count_get(statistics_repository: StatisticsRepository = Depends(get_statistics_repository)):
    count =  statistics_repository.count()
    return count

@router.get("/count")
async def count_between(start: int, end: int, statistics_repository: StatisticsRepository = Depends(get_statistics_repository)):
    count = statistics_repository.count_between(
        start=datetime.fromtimestamp(start),
        end=datetime.fromtimestamp(end)
    )
    return count
