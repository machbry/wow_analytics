from typing import List
from enum import Enum
from pathlib import Path
import json
from datetime import datetime
import pandas as pd


DATE_FORMAT = "%d-%m-%Y"
ENCODING = 'utf-8'
DATA_STR = "data"
LATEST_STR = "latest"
REPORTS_STR = "reports"
REPORTS_DATA_STR = "report_data"


class FileExt(Enum):
    JSON = '.json'
    CSV = '.csv'
    YAML = '.yaml'
    PYTHON = '.py'
    NOTEBOOK = '.ipynb'


class WowDirs(Enum):
    BASE = Path(__file__).parent.parent.resolve()
    DATA = BASE / DATA_STR
    REPORTS = DATA / REPORTS_STR
    REPORTS_LATEST = REPORTS / LATEST_STR
    REPORTS_DATA = DATA / REPORTS_DATA_STR

    def __init__(self, path: Path):
        super().__init__()
        path.mkdir(parents=True, exist_ok=True)


LATEST_REPORTS_FILE_PATH = WowDirs.REPORTS_LATEST.value / f"{REPORTS_STR}{FileExt.JSON.value}"


def now_to_string() -> str:
    return datetime.now().strftime(DATE_FORMAT)


def get_files_from_folder(folder: Path, extension: FileExt) -> List[Path]:
    return [folder / filename for filename in folder.glob(f"*{extension}")]


def save_guild_reports_to_json(content):
    file_path = WowDirs.REPORTS.value / f"{REPORTS_STR}_{now_to_string()}{FileExt.JSON.value}"

    with open(file_path, 'w', encoding=ENCODING) as f:
        json.dump(content, f)

    with open(LATEST_REPORTS_FILE_PATH, 'w', encoding=ENCODING) as f:
        json.dump(content, f)


def load_latest_reports() -> pd.DataFrame:
    with open(LATEST_REPORTS_FILE_PATH, 'r', encoding=ENCODING) as f:
        guild_reports = json.load(f)
    return pd.DataFrame(guild_reports)


def save_report_data_to_json(content, code):
    file_path = WowDirs.REPORTS_DATA.value / f"{str(code)}{FileExt.JSON.value}"
    with open(file_path, 'w', encoding=ENCODING) as f:
        json.dump(content, f)


def get_reports_code_saved() -> List[str]:
    reports_data_files = get_files_from_folder(folder=WowDirs.REPORTS_DATA.value, extension=FileExt.JSON.value)
    return [json_path.stem for json_path in reports_data_files]


def load_reports_data() -> dict:
    reports_data_files = get_files_from_folder(folder=WowDirs.REPORTS_DATA.value, extension=FileExt.JSON.value)
    reports_data = {}
    for json_path in reports_data_files:
        code = json_path.stem
        with open(json_path, 'r', encoding=ENCODING) as f:
            reports_data[code] = json.load(f)
    return reports_data


def save_df_to_csv(df: pd.DataFrame, file_name: str):
    df.to_csv(WowDirs.DATA.value / f"{file_name}_{now_to_string()}{FileExt.CSV.value}")
