import json
from typing import List

from wlogs.storage import JSONFormat, BatchContainer, DATA_DIRECTORY


class ReportDataContainer(BatchContainer):
    def __init__(self):
        super().__init__(name="report_data", storage_file_format=JSONFormat(), parent=DATA_DIRECTORY)

    def extract(self) -> dict:
        reports_data_files = self.all_files_stored()
        reports_data = {}
        for json_path in reports_data_files:
            code = json_path.stem
            with open(json_path, 'r', encoding=self._storage_file_format.encoding) as f:
                reports_data[code] = json.load(f)
        return reports_data

    def reports_codes_stored(self) -> List[str]:
        return self.all_filenames_stored()
