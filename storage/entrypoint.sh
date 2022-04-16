#!/bin/bash

source /venv/bin/activate
(cd src && python -m storage.main /app/config/local_config.json)