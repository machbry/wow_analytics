from wlogs.datalake import StorageFormat, Lake


class ReportsLake(Lake):
    def __init__(self):
        super().__init__(name="reports", storage_format=StorageFormat.json, latest=True)
