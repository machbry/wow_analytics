from enum import Enum
import os
from pathlib import Path
import json
from datetime import datetime


DATE_FORMAT = "%d-%m-%Y"


# TODO : create these directories if they don't exist
class WowPaths(Enum):
    BASE_PATH = Path(__file__).parent.parent.resolve()
    DATA = os.path.join(BASE_PATH, "data")
    REPORTS = os.path.join(DATA, "reports")


def now_to_string() -> str:
    return datetime.now().strftime(DATE_FORMAT)


def save_guild_reports_to_json(content, guild_id: int):
    file_path = os.path.join(WowPaths.REPORTS.value, f"{str(guild_id)}_reports_{now_to_string()}.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(content, f)
