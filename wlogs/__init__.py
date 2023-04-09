from .api import graphQL_client_from_json
from .files_storage import save_guild_reports_to_json, load_latest_reports, save_report_data_to_json, load_reports_data, \
    save_df_to_csv, get_reports_code_saved
from .queries import query_game_zones_on_page, query_game_specs, query_reports_on_page, query_report


GUILD_ID = 505778  # Rush N Wipe Again on Auberdine
DEFAULT_ZONE_ID = 603  # Ulduar
