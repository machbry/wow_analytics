from .api import graphQL_client_from_json
from .queries import query_game_zones_on_page, query_game_specs, query_reports_on_page, query_report
from .storage import FileFormat, CSVFormat, JSONFormat
from .containers import ReportsLake, ReportDataLake


GUILD_ID = 505778  # Rush N Wipe Again on Auberdine
DEFAULT_ZONE_ID = 603  # Ulduar
