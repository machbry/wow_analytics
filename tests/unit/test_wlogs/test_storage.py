from unittest.mock import Mock

import pytest

import wlogs as wl


@pytest.mark.parametrize("container, now_date, custom_filename", [
    ("json_batch_container", "19-06-1988", "test_file"),
    ("json_batch_container", "19-06-1988", None),
    ("csv_latest_container", "15-11-1995", "another_test_file"),
    ("csv_latest_container", "15-11-1995", None)])
def test_new_file_path(container, now_date, custom_filename, request):
    container = request.getfixturevalue(container)
    wl.storage.now_to_string = Mock(return_value=now_date)

    if custom_filename:
        path_expected = container.directory / (
                    custom_filename + container.storage_file_format.suffix)
    else:
        path_expected = container.directory / (container.name + "_" + now_date
                                                          + container.storage_file_format.suffix)

    assert container.new_file_path(custom_filename=custom_filename) == path_expected
