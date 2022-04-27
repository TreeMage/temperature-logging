#!/bin/bash

source /venv/bin/activate
(cd src && python -m thermometer.main /app/config/local_config.json)