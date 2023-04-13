from typing import Union, List, Any
from pathlib import Path
from datetime import datetime
import json
import pandas as pd


DATA_DIRECTORY: Path = Path(__file__).parent.parent.resolve() / "data"


def now_to_string(date_format: str) -> str:
    return datetime.now().strftime(date_format)


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

    def write_file(self, content: Any, path: Path):
        pass


class CSVFormat(FileFormat):
    def __init__(self, encoding: str = "utf-8", sep: str = ";"):
        super().__init__(suffix='.csv', encoding=encoding)
        self._sep = sep

    def write_file(self, content: pd.DataFrame, path: Path) -> None:
        content.to_csv(path, sep=self._sep)


class JSONFormat(FileFormat):
    def __init__(self, encoding: str = "utf-8"):
        super().__init__(suffix='.json', encoding=encoding)

    def write_file(self, content: Union[list, dict], path: Path) -> None:
        with open(path, 'w', encoding=self._encoding) as f:
            json.dump(content, f)


class Container:
    def __init__(self, name: str, storage_file_format: FileFormat, parent: Path):
        self._name = name
        self._storage_file_format = storage_file_format
        self._parent = parent
        self._directory: Path = parent / name
        self._directory.mkdir(parents=True, exist_ok=True)

    def new_file_path(self, custom_filename: Union[str, None]) -> Path:
        filename = f"{custom_filename}{self._storage_file_format.suffix}" if custom_filename else \
            f"{self._name}_{now_to_string(date_format='%d-%m-%Y')}{self._storage_file_format.suffix}"
        return self._directory / filename

    def store(self, content, custom_filename: Union[str, None] = None):
        self._storage_file_format.write_file(content=content, path=self.new_file_path(custom_filename=custom_filename))


class BatchContainer(Container):
    def __init__(self, name: str, storage_file_format: FileFormat, parent: Path):
        super().__init__(name=name, storage_file_format=storage_file_format, parent=parent)

    def all_files_stored(self) -> List[Path]:
        return [self._directory / filename for filename in self._directory.glob(f"*{self._storage_file_format.suffix}")]

    def all_filenames_stored(self) -> List[str]:
        return [path.stem for path in self.all_files_stored()]


class LatestContainer(Container):
    def __init__(self, name: str, storage_file_format: FileFormat, parent: Path):
        super().__init__(name=name, storage_file_format=storage_file_format, parent=parent)
        self._latest_directory: Path = self._directory / "latest"
        self._latest_directory.mkdir(parents=True, exist_ok=True)

    @property
    def latest_file_path(self) -> Union[Path, None]:
        latest_filename = f"{self._name}{self._storage_file_format.suffix}"
        return self._latest_directory / latest_filename

    def store(self, content, custom_filename: Union[str, None] = None):
        super().store(content=content, custom_filename=custom_filename)
        self._storage_file_format.write_file(content=content, path=self.latest_file_path)
