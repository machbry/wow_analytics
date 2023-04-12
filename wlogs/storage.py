from typing import Union, List, Any
from dataclasses import dataclass
from pathlib import Path
from enum import Enum
from datetime import datetime
import json
import pandas as pd


DATA_DIRECTORY: Path = Path(__file__).parent.parent.resolve() / "data"
DATE_FORMAT = "%d-%m-%Y"
ENCODING = 'utf-8'
CSV_SEP = ";"


def now_to_string(date_format: str) -> str:
    return datetime.now().strftime(date_format)


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

    def all_files_stored(self) -> List[Path]:
        return [self._directory / filename for filename in self._directory.glob(f"*{self._storage_format.value}")]

    def all_filenames_stored(self) -> List[str]:
        return [path.stem for path in self.all_files_stored()]

    def now_to_string(self) -> str:
        return datetime.now().strftime(self._date_format)

    def new_file_path(self, custom_filename: str) -> Path:
        filename = f"{custom_filename}{self._storage_format.value}" if custom_filename else \
            f"{self._name}_{self.now_to_string()}{self._storage_format.value}"
        return self._directory / filename

    def store_to_json(self, json_content: Union[list, dict], path: Path) -> None:
        with open(path, 'w', encoding=self._encoding) as f:
            json.dump(json_content, f)

    def store_to_csv(self, df: pd.DataFrame, path: Path) -> None:
        df.to_csv(path, sep=self._csv_sep)

    def store(self, content: Union[list, dict, pd.DataFrame], custom_filename: str = None) -> None:
        if self._storage_format == StorageFormat.json:
            assert isinstance(content, (list, dict))
            self.store_to_json(json_content=content, path=self.new_file_path(custom_filename=custom_filename))
            if self._latest:
                self.store_to_json(json_content=content, path=self.latest_file_path)
        elif self._storage_format == StorageFormat.csv:
            assert isinstance(content, pd.DataFrame)
            self.store_to_csv(df=content, path=self.new_file_path(custom_filename=custom_filename))
            if self._latest:
                self.store_to_csv(df=content,path=self.latest_file_path)


class FileFormat:
    def __init__(self, suffix: str, encoding: str):
        self._suffix = suffix
        self._encoding = encoding

    @property
    def suffix(self) -> str:
        return self._suffix

    @property
    def encoding(self) -> str:
        return self._encoding


class CSVFormat(FileFormat):
    def __init__(self, encoding: str = "utf-8", sep: str = ";"):
        super().__init__(suffix='.csv', encoding=encoding)
        self._sep = sep


class JSONFormat(FileFormat):
    def __init__(self, encoding: str = "utf-8"):
        super().__init__(suffix='.json', encoding=encoding)


class ContainerInterface:
    def __init__(self, name: str, storage_file_format: FileFormat, parent: Path):
        self._name = name
        self._storage_file_format = storage_file_format
        self._parent = parent
        self._directory: Path = parent / name
        self._directory.mkdir(parents=True, exist_ok=True)

    def new_file_path(self, custom_filename: Union[str, None] = None) -> Path:
        filename = f"{custom_filename}{self._storage_file_format.suffix}" if custom_filename else \
            f"{self._name}_{now_to_string(date_format='%d-%m-%Y')}{self._storage_file_format.suffix}"
        return self._directory / filename


class BatchContainer(ContainerInterface):
    def __init__(self, name: str, storage_file_format: FileFormat, parent: Path):
        super().__init__(name=name, storage_file_format=storage_file_format, parent=parent)

    def all_files_stored(self) -> List[Path]:
        return [self._directory / filename for filename in self._directory.glob(f"*{self._storage_file_format.suffix}")]

    def all_filenames_stored(self) -> List[str]:
        return [path.stem for path in self.all_files_stored()]


class LatestContainer(ContainerInterface):
    def __init__(self, name: str, storage_file_format: FileFormat, parent: Path):
        super().__init__(name=name, storage_file_format=storage_file_format, parent=parent)
        self._latest_directory: Path = self._directory / "latest"

    @property
    def latest_file_path(self) -> Union[Path, None]:
        latest_filename = f"{self._name}{self._storage_file_format.suffix}"
        return self._latest_directory / latest_filename
