from enum import Enum
import os
from typing import List
from pathlib import Path
import json
from datetime import datetime


DATE_FORMAT = "%d-%m-%Y"
LATEST_DIR_NAME = "latest"


class WowPaths(Enum):
    BASE_PATH = Path(__file__).parent.parent.resolve()
    DATA = os.path.join(BASE_PATH, "data")
    REPORTS = os.path.join(DATA, "reports")


def now_to_string() -> str:
    return datetime.now().strftime(DATE_FORMAT)


def check_and_create_dirs(directories: List[Path]):
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)


def save_guild_reports_to_json(content, guild_id: int):
    reports_dir = WowPaths.REPORTS.value
    reports_latest_dir = os.path.join(reports_dir, LATEST_DIR_NAME)

    file_path = os.path.join(reports_dir, f"{str(guild_id)}_reports_{now_to_string()}.json")
    latest_file_path = os.path.join(reports_latest_dir, f"{str(guild_id)}_reports_latest.json")

    check_and_create_dirs([reports_dir, reports_latest_dir])

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(content, f)

    with open(latest_file_path, 'w', encoding='utf-8') as f:
        json.dump(content, f)
