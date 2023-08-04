from pathlib import Path
import pytest
from wlogs.storage import BatchContainer, JSONFormat

TESTS_DATA_PATH = Path(__file__).parent.resolve() / "data"
TESTS_DATA_PATH.mkdir(parents=True, exist_ok=True)


@pytest.fixture
def json_batch_container():
    return BatchContainer(**{"name": "test_batch",
                             "storage_file_format": JSONFormat(),
                             "parent": TESTS_DATA_PATH})
