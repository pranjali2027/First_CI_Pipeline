import importlib

module = importlib.import_module("28_set_intersection")
set_intersection = module.set_intersection


def test_normal_intersection():
    assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}


def test_no_common_elements():
    assert set_intersection({1, 2}, {3, 4}) == set()


def test_identical_sets():
    assert set_intersection({1, 2, 3}, {1, 2, 3}) == {1, 2, 3}


def test_first_set_empty():
    assert set_intersection(set(), {1, 2}) == set()


def test_second_set_empty():
    assert set_intersection({1, 2}, set()) == set()


def test_both_sets_empty():
    assert set_intersection(set(), set()) == set()


def test_single_common_element():
    assert set_intersection({1, 2}, {2, 3}) == {2}