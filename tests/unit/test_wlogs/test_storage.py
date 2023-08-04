from unittest.mock import Mock

import wlogs as wl


def test_new_file_path(json_batch_container):
    now_date = "19-06-1988"
    wl.storage.now_to_string = Mock(return_value=now_date)

    path_expected = json_batch_container.directory / (json_batch_container.name + "_" + now_date
                                                      + json_batch_container.storage_file_format.suffix)
    assert json_batch_container.new_file_path(custom_filename=None) == path_expected

    custom_filename = "test_file"
    path_expected = json_batch_container.directory / (custom_filename + json_batch_container.storage_file_format.suffix)
    assert json_batch_container.new_file_path(custom_filename=custom_filename) == path_expected
