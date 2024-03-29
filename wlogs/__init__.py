import os
from dotenv import load_dotenv

load_dotenv()

from .queries import query_item, query_game_zones_on_page, query_game_specs, query_reports_on_page, query_report
from .storage import ROOT_DIRECTORY, DATA_DIRECTORY, TEMP_DIRECTORY
from .containers import ReportsContainer, ReportDataContainer, RaidLootsContainer, BisListContainer
from .conf import game_settings_from_json
from .database import engine
from .backoffice import start_back_office


GUILD_ID = os.environ["GUILD_ID"]
DEFAULT_ZONE_ID = os.environ["DEFAULT_ZONE_ID"]
