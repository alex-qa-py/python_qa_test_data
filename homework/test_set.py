import pytest


@pytest.fixture()
def data_set():
    return {1, 2, 3, 5, 5, 6}


def test_union(data_set):
    union_sets = data_set.union({1, 2, 3, 9})
    assert len(union_sets) == 6


def test_add(data_set):
    data_set.add(7)
    assert data_set == {1, 2, 3, 5, 6, 7}


def test_remove(data_set):
    data_set.remove(2)
    assert data_set == {1, 3, 5, 6}


def test_clear(data_set):
    data_set.clear()
    assert len(data_set) == 0


@pytest.mark.parametrize("test_set, other_set, expected_result", [
    ({1, 2}, {2, 4}, {1, 4}),
    ({1, 6}, {2, 7}, {1, 2, 6, 7}),
    ({1, 3}, {4, 3}, {1, 4})
])
def test_(test_set: set, other_set, expected_result):
    test_set.symmetric_difference_update(other_set)
    assert test_set == expected_result
