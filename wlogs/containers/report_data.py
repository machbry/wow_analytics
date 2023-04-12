import json

from wlogs.storage import StorageFormat, Lake


class ReportDataLake(Lake):
    def __init__(self):
        super().__init__(name="report_data", storage_format=StorageFormat.json, latest=False)

    def extract_data(self) -> dict:
        reports_data_files = self.all_files_stored()
        reports_data = {}
        for json_path in reports_data_files:
            code = json_path.stem
            with open(json_path, 'r', encoding=self._encoding) as f:
                reports_data[code] = json.load(f)
        return reports_data
