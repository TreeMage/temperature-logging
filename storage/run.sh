#!/bin/bash
(cd src && \
nohup poetry run python -m storage.main ../config/local_config.json &)
