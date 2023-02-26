from .api import graphQL_client_from_json
from .file_manager import save_guild_reports_to_json, load_latest_reports, save_report_data_to_json
from .queries import query_reports_on_page, query_report


CLIENT = graphQL_client_from_json()
GUILD_ID = 505778
