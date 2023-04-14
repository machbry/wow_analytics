from typing import List, Dict

from wlogs.storage import JSONFormat, BatchContainer, DATA_DIRECTORY


class ReportDataContainer(BatchContainer):
    def __init__(self):
        super().__init__(name="report_data", storage_file_format=JSONFormat(), parent=DATA_DIRECTORY)

    def extract(self) -> Dict[str, Dict]:
        return super().extract()

    def reports_codes_stored(self) -> List[str]:
        return self.all_filenames_stored()
