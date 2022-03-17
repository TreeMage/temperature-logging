from dataclasses import dataclass
from datetime import datetime
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Measurement:
    temperature: float
    humidity: float
    timestamp: datetime