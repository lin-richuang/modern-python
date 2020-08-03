"""Fixtures placed in a conftest.py file are discovered automatically,
and test modules at the same directory level can use them without explicit import.
"""


import pytest


# The unittest.mock standard library allows you to replace parts of your system under test with mock objects.
# Use it via the pytest-mock plugin, which integrates the library with pytest:
@pytest.fixture
def mock_requests_get(mocker):
    """Mocking not only speeds up your test suite, or lets you hack offline on a plane or train.
    By virtue of having a fixed, or deterministic, return value, the mock also enables you to write repeatable tests.
    """
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock
