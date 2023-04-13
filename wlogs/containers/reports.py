import pandas as pd
import json

from wlogs.storage import LatestContainer, JSONFormat, DATA_DIRECTORY


class ReportsContainer(LatestContainer):
    def __init__(self):
        super().__init__(name="reports", storage_file_format=JSONFormat(), parent=DATA_DIRECTORY)

    def get_latest(self) -> pd.DataFrame:
        with open(self.latest_file_path, 'r', encoding=self._storage_file_format.encoding) as f:
            reports = json.load(f)
        return pd.DataFrame(reports)
