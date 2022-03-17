from datetime import datetime
from thermometer.model.measurement import Measurement


class MeasurementService:
    def measure(self) -> Measurement:
        return Measurement(
            10,
            10,
            datetime.now()
        )