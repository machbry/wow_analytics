from typing import List
from enum import Enum
import os
from pathlib import Path
import json
from datetime import datetime
import pandas as pd


DATE_FORMAT = "%d-%m-%Y"
DATA_STR = "data"
REPORTS_STR = "reports"
LATEST_STR = "latest"
ENCODING = 'utf-8'


class FileExt(Enum):
    JSON = '.json'
    CSV = '.csv'
    YAML = '.yaml'
    PYTHON = '.py'
    NOTEBOOK = '.ipynb'


class WowDirs(Enum):
    BASE = Path(__file__).parent.parent.resolve()
    DATA = os.path.join(BASE, DATA_STR)
    REPORTS = os.path.join(DATA, REPORTS_STR)
    REPORTS_LATEST = os.path.join(REPORTS, LATEST_STR)
    REPORTS_DATA = os.path.join(REPORTS, DATA_STR)

    def __init__(self, path: Path):
        super().__init__()
        if not os.path.exists(path):
            os.makedirs(path)


LATEST_REPORTS_FILE_PATH = os.path.join(WowDirs.REPORTS_LATEST.value, f"{REPORTS_STR}{FileExt.JSON.value}")


def now_to_string() -> str:
    return datetime.now().strftime(DATE_FORMAT)


def get_files_from_folder(folder: Path, extension: FileExt) -> List[Path]:
    seeked_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(extension):
                seeked_files.append(os.path.join(root, file))
    return seeked_files


def save_guild_reports_to_json(content):
    file_path = os.path.join(WowDirs.REPORTS.value, f"{REPORTS_STR}_{now_to_string()}{FileExt.JSON.value}")

    with open(file_path, 'w', encoding=ENCODING) as f:
        json.dump(content, f)

    with open(LATEST_REPORTS_FILE_PATH, 'w', encoding=ENCODING) as f:
        json.dump(content, f)


def load_latest_reports() -> pd.DataFrame:
    with open(LATEST_REPORTS_FILE_PATH, 'r', encoding=ENCODING) as f:
        guild_reports = json.load(f)
    return pd.DataFrame(guild_reports)


def save_report_data_to_json(content, code):
    file_path = os.path.join(WowDirs.REPORTS_DATA.value, f"{str(code)}{FileExt.JSON.value}")
    with open(file_path, 'w', encoding=ENCODING) as f:
        json.dump(content, f)


def load_reports_data() -> dict:
    reports_data_files = get_files_from_folder(folder=WowDirs.REPORTS_DATA.value, extension=FileExt.JSON.value)
    reports_data = {}
    for json_path in reports_data_files:
        code = os.path.splitext(os.path.basename(json_path))[0]
        with open(json_path, 'r', encoding=ENCODING) as f:
            reports_data[code] = json.load(f)
    return reports_data


def save_df_to_csv(df: pd.DataFrame, file_name: str):
    df.to_csv(os.path.join(WowDirs.DATA.value, f"{file_name}_{now_to_string()}{FileExt.CSV.value}"))
