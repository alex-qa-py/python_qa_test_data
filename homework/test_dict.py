import pytest


@pytest.fixture()
def data_dict():
    return {"name": "Alex", "last_name": "Krylov"}


def test_values(data_dict):
    assert list(data_dict.values()) == ["Alex", "Krylov"]


def test_keys(data_dict):
    assert list(data_dict.keys()) == ["name", "last_name"]


def test_clear(data_dict):
    data_dict.clear()
    assert data_dict == {}
    assert len(data_dict) == 0


def test_pop(data_dict):
    data_dict.pop("name")
    assert data_dict == {"last_name": "Krylov"}


@pytest.mark.parametrize("main_dict, other_dict, expected_result", [
    ({"city": "SPB", "office": "322324"}, {"function": "QA"}, {"city": "SPB", "office": "322324", "function": "QA"}),
    ({"city": "MSK", "office": "34342d3"}, {"function": "TeamLead"},
     {"city": "MSK", "office": "34342d3", "function": "TeamLead"})
])
def test_(main_dict, other_dict, expected_result):
    main_dict.update(other_dict)
    assert main_dict == expected_result
