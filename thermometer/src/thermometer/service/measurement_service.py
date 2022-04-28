from datetime import datetime
from typing import Tuple
from thermometer.model.config import MeasurementConfig
from thermometer.model.measurement import Measurement
import time
import board
import adafruit_dht

class MeasurementService:

    def __init__(self, measurement_config: MeasurementConfig) -> None:
        self.config = measurement_config


        pin = getattr(board, self.config.pin)
        if pin is None:
            raise KeyError(f"Pin '{self.config.pin}' is invalid.")

        self.device = adafruit_dht.DHT22(pin)

    def measure(self) -> Measurement:
        measurements = []
        for _ in range(self.config.num_measurements):
            measurements.append(self._measure())

        avg_temp = sum(map(lambda m: m[0], measurements)) / self.config.num_measurements
        avg_humidity = sum(map(lambda m: m[1], measurements)) / self.config.num_measurements

        return Measurement(
            temperature=avg_temp,
            humidity=avg_humidity,
            timestamp=datetime.now()
        )
    

    def _measure(self) -> Tuple[float, float]:
        while True:
            try:
                temp = self.device.temperature
                humidity = self.device.humidity
                return (temp, humidity)
            except RuntimeError as error:
                time.sleep(0.01)
                continue
            except Exception as error:
                self.device.exit()
                raise error
