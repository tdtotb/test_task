import pytest

from config import TESTING_DATA
from framework.helper import load_params_from_json


@pytest.fixture
def get_body_from_json(name):
    body = load_params_from_json(TESTING_DATA)
    return body[name]
