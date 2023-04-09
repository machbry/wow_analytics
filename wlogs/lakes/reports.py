import json

from wlogs.datalake import StorageFormat, Lake, now_to_string


class ReportsLake(Lake):
    def __init__(self):
        super().__init__(name="reports", storage_format=StorageFormat.json, latest=True)

    def store(self, content):
        filename = f"{self._name}_{now_to_string()}{self._storage_format.value}"
        with open(self._directory / filename, 'w', encoding=self._encoding) as f:
            json.dump(content, f)

        latest_filename = f"{self._name}{self._storage_format.value}"
        with open(self._latest_directory / latest_filename, 'w', encoding=self._encoding) as f:
            json.dump(content, f)
