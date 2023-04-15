import pandas as pd
from typing import List
from wlogs.storage import CSVFormat, LatestContainer, DATA_DIRECTORY


class RaidLootsContainer(LatestContainer):
    def __init__(self):
        super().__init__(name="raid_loots", storage_file_format=CSVFormat(), parent=DATA_DIRECTORY)

    def extract(self) -> pd.DataFrame:
        return super().extract()

    def get_all_items_id(self) -> List[int]:
        df = self.extract()
        return [int(item_id) for item_id in df['item_id'].unique()]

