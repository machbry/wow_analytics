import logging
from pathlib import Path

from .conf import logging_basic_config_from_json

LOGS_FILEPATH = Path(__file__).parent.parent.resolve() / 'data' / 'logs'
LOGS_FILEPATH.mkdir(parents=True, exist_ok=True)


class Logger:
    def __init__(self):
        params = logging_basic_config_from_json().__dict__
        for param, value in params.items():
            if param == 'level':
                params[param] = getattr(logging, value)
            elif param == 'filename':
                params[param] = LOGS_FILEPATH / value

        logging.basicConfig(**params)
        self._logger = logging.getLogger(name='wlogs')

    def get(self):
        return self._logger
