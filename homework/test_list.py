import pytest


@pytest.fixture()
def data_list():
    return [1, 2, 2, 3, 4]


def test_count(data_list):
    assert data_list.count(2) == 2


def test_reverse(data_list):
    data_list.reverse()
    assert data_list == [4, 3, 2, 2, 1]


def test_clear(data_list):
    data_list.clear()
    assert len(data_list) == 0


def test_append(data_list):
    data_list.append(5)
    assert len(data_list) == 6
    assert data_list == [1, 2, 2, 3, 4, 5]


@pytest.mark.parametrize("list_int, expected_result", [([1, 3, 2], [1, 2, 3]), ([5, 8, 1], [1, 5, 8])])
def test_sort(list_int, expected_result):
    list_int.sort()
    assert list_int == expected_result
