#!/bin/bash
(cd src && \
nohup poetry run python -m thermometer.main ../config/local_config.json &)
