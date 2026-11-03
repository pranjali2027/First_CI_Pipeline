import importlib

module = importlib.import_module("27_rotate_list")
rotate_list = module.rotate_list


def test_rotate_right():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_rotate_one_position():
    assert rotate_list([1, 2, 3], 1) == [3, 1, 2]


def test_rotate_by_zero():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]


def test_k_larger_than_list_length():
    assert rotate_list([1, 2, 3], 5) == [2, 3, 1]


def test_negative_k():
    assert rotate_list([1, 2, 3, 4], -1) == [2, 3, 4, 1]


def test_empty_list():
    assert rotate_list([], 2) == []


def test_single_element():
    assert rotate_list([7], 5) == [7]


def test_original_list_unchanged():
    items = [1, 2, 3]
    rotate_list(items, 1)
    assert items == [1, 2, 3]