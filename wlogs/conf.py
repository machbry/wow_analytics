import os
import re
from pathlib import Path
from dataclasses import dataclass
import json
import yaml


ROOT_DIRECTORY: Path = Path(re.sub(r'^/?(?:mnt/)?[a-z]', '', os.environ["WA_ROOT_DIR"])).resolve()
CONF_DIRECTORY: Path = ROOT_DIRECTORY / "conf"


def logging_config_from_yaml(path: Path = CONF_DIRECTORY / "logs.yaml") -> dict:
    with open(path, 'r') as f:
        return yaml.safe_load(f.read())


@dataclass
class GameSettings:
    _installation_directory: str
    _version: str

    @property
    def installation_path(self) -> Path:
        return Path(self._installation_directory)

    @property
    def version(self) -> str:
        return self._version


def game_settings_from_json(path: Path = CONF_DIRECTORY / "game.json") -> GameSettings:
    with open(path, 'r') as f:
        return GameSettings(**json.load(f))
