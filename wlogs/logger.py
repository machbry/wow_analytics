import logging
from logging.config import dictConfig
from pathlib import Path

from .conf import logging_config_from_yaml

LOGS_FILEPATH = Path(__file__).parent.parent.resolve() / 'data' / 'logs'
LOGS_FILEPATH.mkdir(parents=True, exist_ok=True)


class Logger:
    def __init__(self):
        config = logging_config_from_yaml()
        dictConfig(config)
        self._logger = logging.getLogger(name='wlogs')

    def get(self):
        return self._logger
