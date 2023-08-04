from pathlib import Path
from unittest.mock import Mock

import wlogs as wl
from wlogs.storage import BatchContainer, JSONFormat

TESTS_WLOGS_DATA_PATH = Path(__file__).parent.resolve() / "data"
TESTS_WLOGS_DATA_PATH.mkdir(parents=True, exist_ok=True)
BATCH_CONTAINER_NAME = "test_batch"
NOW_DATE = "19-06-1988"
wl.storage.now_to_string = Mock(return_value=NOW_DATE)

test_batch_container = BatchContainer(name=BATCH_CONTAINER_NAME,
                                      storage_file_format=JSONFormat(),
                                      parent=TESTS_WLOGS_DATA_PATH)


def test_new_file_path():
    path_expected = TESTS_WLOGS_DATA_PATH / BATCH_CONTAINER_NAME / (BATCH_CONTAINER_NAME + "_" + NOW_DATE + ".json")
    assert test_batch_container.new_file_path(custom_filename=None) == path_expected

    custom_filename = "test_file"
    path_expected = TESTS_WLOGS_DATA_PATH / BATCH_CONTAINER_NAME / (custom_filename + ".json")
    assert test_batch_container.new_file_path(custom_filename=custom_filename) == path_expected
