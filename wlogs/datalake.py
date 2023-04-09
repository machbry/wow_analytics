from pathlib import Path
from enum import Enum
from datetime import datetime

DATA_DIRECTORY: Path = Path(__file__).parent.parent.resolve() / "data"
DATE_FORMAT = "%d-%m-%Y"
ENCODING = 'utf-8'


class StorageFormat(Enum):
    json = '.json'
    csv = '.csv'


def now_to_string() -> str:
    return datetime.now().strftime(DATE_FORMAT)


class Lake:
    def __init__(self, name: str, storage_format: StorageFormat, latest: bool, parent: Path = DATA_DIRECTORY,
                 date_format: str = DATE_FORMAT, encoding: str = ENCODING):
        self._name: str = name
        self._storage_format: StorageFormat = storage_format
        self._latest: bool = latest
        self._parent: Path = parent
        self._date_format: str = date_format
        self._encoding: str = encoding

        self._directory: Path = parent / name
        self._directory.mkdir(parents=True, exist_ok=True)
        self._latest_directory: Path = self._directory / "latest" if latest else None
