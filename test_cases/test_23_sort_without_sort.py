
import importlib

module = importlib.import_module("23_sort_without_sort")
bubble_sort = module.bubble_sort

def test_unsorted_list():
    assert bubble_sort([5, 2, 8, 1]) == [1, 2, 5, 8]

def test_already_sorted_list():
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_reverse_order():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_duplicate_numbers():
    assert bubble_sort([4, 2, 4, 1, 2]) == [1, 2, 2, 4, 4]

def test_empty_list():
    assert bubble_sort([]) == []

def test_single_element():
    assert bubble_sort([7]) == [7]

def test_original_list_unchanged():
    numbers = [5, 3, 1]
    bubble_sort(numbers)
    assert numbers == [5, 3, 1]