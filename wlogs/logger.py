import logging
from logging.config import dictConfig

from .conf import logging_config_from_yaml


class Logger:
    def __init__(self):
        config = logging_config_from_yaml()
        dictConfig(config)
        self._logger = logging.getLogger(name='wlogs')

    def get(self):
        return self._logger
