import pandas as pd
import json

from wlogs.datalake import StorageFormat, Lake


class ReportsLake(Lake):
    def __init__(self):
        super().__init__(name="reports", storage_format=StorageFormat.json, latest=True)

    def get_latest(self) -> pd.DataFrame:
        with open(self.latest_file_path, 'r', encoding=self._encoding) as f:
            reports = json.load(f)
        return pd.DataFrame(reports)
