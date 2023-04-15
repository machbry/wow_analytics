from typing import List
from wlogs.storage import LatestContainer, JSONFormat, DATA_DIRECTORY


class BisListContainer(LatestContainer):
    def __init__(self):
        super().__init__(name="bis_list", storage_file_format=JSONFormat(), parent=DATA_DIRECTORY)

    def extract(self) -> dict:
        return super().extract()

    def get_all_items_id(self) -> List[int]:
        bis_list_json = super().extract()
        return [int(id) for id in bis_list_json.keys()]
