from pathlib import Path
from dataclasses import dataclass
import json

CONF_DIRECTORY: Path = Path(__file__).parent.parent.resolve() / "conf"


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
