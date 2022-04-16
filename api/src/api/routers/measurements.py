from datetime import datetime
from fastapi import APIRouter, Depends
from api.dependencies import get_measurement_repository

from api.serivce.repository import MeasurementRepository

router = APIRouter(
    prefix="/measurements",
    tags=["measurements"]
)


@router.get("/measurements")
async def between(start: int, end: int, measurement_repository: MeasurementRepository = Depends(get_measurement_repository)):
    measurements = measurement_repository.between(
        start=datetime.fromtimestamp(start),
        end=datetime.fromtimestamp(end)
    )
    return measurements