import pytest


@pytest.fixture()
def data_string():
    return "Pyt_hon"


def test_upper(data_string):
    assert data_string.upper() == "PYT_HON"


def test_lower(data_string):
    assert data_string.lower() == "pyt_hon"


def test_isdigit(data_string):
    assert data_string.isdigit() == False


def test_rsplit(data_string):
    assert data_string.rsplit("_") == ["Pyt", "hon"]


@pytest.mark.parametrize("string, expected_result", [
    ("abcd", "Abcd"),
    ("aassff", "Aassff"),
    ("alex", "Alex"),
])
def test_reverse(string, expected_result):
    assert string.capitalize() == expected_result
