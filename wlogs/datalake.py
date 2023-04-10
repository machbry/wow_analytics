from typing import Union, List
from pathlib import Path
from enum import Enum
from datetime import datetime
import json
import pandas as pd


DATA_DIRECTORY: Path = Path(__file__).parent.parent.resolve() / "data"
DATE_FORMAT = "%d-%m-%Y"
ENCODING = 'utf-8'
CSV_SEP = ";"


class StorageFormat(Enum):
    json = '.json'
    csv = '.csv'


class Lake:
    def __init__(self, name: str, storage_format: StorageFormat, latest: bool, parent: Path = DATA_DIRECTORY,
                 date_format: str = DATE_FORMAT, encoding: str = ENCODING, csv_sep: str = CSV_SEP):
        self._name: str = name
        self._storage_format: StorageFormat = storage_format
        self._latest: bool = latest
        self._parent: Path = parent
        self._date_format: str = date_format
        self._encoding: str = encoding
        self._csv_sep: str = csv_sep

        self._directory: Path = parent / name
        self._directory.mkdir(parents=True, exist_ok=True)
        self._latest_directory: Union[Path, None] = self._directory / "latest" if latest else None

    @property
    def latest_file_path(self) -> Union[Path, None]:
        latest_filename = f"{self._name}{self._storage_format.value}"
        return self._latest_directory / latest_filename if self._latest else None

    def now_to_string(self) -> str:
        return datetime.now().strftime(self._date_format)

    def new_file_path(self) -> Path:
        filename = f"{self._name}_{self.now_to_string()}{self._storage_format.value}"
        return self._directory / filename

    def store_to_json(self, json_content: Union[list, dict], path: Path):
        with open(path, 'w', encoding=self._encoding) as f:
            json.dump(json_content, f)

    def store_to_csv(self, df: pd.DataFrame, path: Path):
        df.to_csv(path, sep=self._csv_sep)

    def store(self, content: Union[list, dict, pd.DataFrame]):
        if self._storage_format == StorageFormat.json:
            assert isinstance(content, (list, dict))
            self.store_to_json(json_content=content, path=self.new_file_path())
            if self._latest:
                self.store_to_json(json_content=content, path=self.latest_file_path)
        elif self._storage_format == StorageFormat.csv:
            assert isinstance(content, pd.DataFrame)
            self.store_to_csv(df=content, path=self.new_file_path())
            if self._latest:
                self.store_to_csv(df=content,path=self.latest_file_path)
