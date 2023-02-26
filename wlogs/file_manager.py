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


LATEST_REPORTS_FILE_PATH = os.path.join(WowDirs.REPORTS_LATEST.value, f"{REPORTS_STR}.json")


def now_to_string() -> str:
    return datetime.now().strftime(DATE_FORMAT)


def save_guild_reports_to_json(content):
    file_path = os.path.join(WowDirs.REPORTS.value, f"{REPORTS_STR}_{now_to_string()}.json")

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(content, f)

    with open(LATEST_REPORTS_FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(content, f)


def load_latest_reports() -> pd.DataFrame:
    with open(LATEST_REPORTS_FILE_PATH, 'r', encoding='utf-8') as f:
        guild_reports = json.load(f)
    return pd.DataFrame(guild_reports)


def save_report_data_to_json(content, code):
    file_path = os.path.join(WowDirs.REPORTS_DATA.value, f"{str(code)}.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(content, f)
