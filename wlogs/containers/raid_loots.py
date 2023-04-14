import pandas as pd

from wlogs.storage import CSVFormat, LatestContainer, DATA_DIRECTORY


class RaidLootsContainer(LatestContainer):
    def __init__(self):
        super().__init__(name="raid_loots", storage_file_format=CSVFormat(), parent=DATA_DIRECTORY)

    def extract(self) -> pd.DataFrame:
        return super().extract()
