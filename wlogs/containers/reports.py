import pandas as pd

from wlogs.storage import LatestContainer, JSONFormat, DATA_DIRECTORY


class ReportsContainer(LatestContainer):
    def __init__(self):
        super().__init__(name="reports", storage_file_format=JSONFormat(), parent=DATA_DIRECTORY)

    def extract(self) -> pd.DataFrame:
        reports = super().extract()
        reports_df = pd.DataFrame(reports)
        reports_df['guild'] = reports_df['guild'].apply(lambda x: x['id'])
        return reports_df
