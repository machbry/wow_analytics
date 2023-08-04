from pathlib import Path
import pytest
from wlogs.storage import BatchContainer, JSONFormat
import requests

TESTS_DATA_PATH = Path(__file__).parent.resolve() / "data"
TESTS_DATA_PATH.mkdir(parents=True, exist_ok=True)


@pytest.fixture
def json_batch_container():
    return BatchContainer(**{"name": "test_batch",
                             "storage_file_format": JSONFormat(),
                             "parent": TESTS_DATA_PATH})


@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())

    def stunted_post():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(requests, "post", lambda *args, **kwargs: stunted_post())
