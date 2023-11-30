import pytest
from solutions.lists import *

def test_merge_and_sort_lists():
    assert merge_and_sort_lists([3, 1], [2, 4]) == [1, 2, 3, 4]
    assert merge_and_sort_lists([], [2, 4, 1]) == [1, 2, 4]
    assert merge_and_sort_lists([3], []) == [3]
    assert merge_and_sort_lists([], []) == []

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([4, 4, 4, 4]) == [4]
    assert remove_duplicates([]) == []
    assert remove_duplicates(['a', 'b', 'a', 'c', 'b']) == ['a', 'b', 'c']

def test_is_sublist():
    assert is_sublist([1, 2], [1, 0, 1, 2, 3]) == True
    assert is_sublist([1, 2, 3], [1, 2]) == False
    assert is_sublist([], [1, 2, 3]) == True
    assert is_sublist([1, 2, 3], []) == False

def test_rotate_list():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate_list(['a', 'b', 'c', 'd'], 1) == ['d', 'a', 'b', 'c']
    assert rotate_list([], 2) == []
    assert rotate_list([1], 10) == [1]

def test_generate_numbers():
    assert generate_numbers(5) == [1, 2, 3, 4, 5]
    assert generate_numbers(0) == []
    assert generate_numbers(-1) == []

