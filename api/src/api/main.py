from pathlib import Path
from fastapi import FastAPI
from loguru import logger
from routers import statistics

app = FastAPI()
app.include_router(statistics.router)

