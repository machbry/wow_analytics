from .api import GraphQLClient, graphQL_client_from_json
from .file_manager import WowDirs, save_guild_reports_to_json, load_latest_reports, save_report_data_to_json
from .queries import query_reports_on_page, query_report


# TODO : create conf file with guild information
GUILD_ID = 505778
