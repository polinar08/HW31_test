from utils import arrs


def test_get_existing_index():
    assert arrs.get([1, 2, 3], 1, "test") == 2

def test_get_non_existing_index():
    assert arrs.get([1, 2, 3], 5, "test") == "test"

def test_get_negative_index():
    assert arrs.get([1, 2, 3], -1, "test") == "test"

def test_get_empty_array():
    assert arrs.get([], 0, "test") == "test"

def test_my_slice_full_range():
    assert arrs.my_slice([1, 2, 3, 4], start=0, end=4) == [1, 2, 3, 4]

def test_my_slice_partial_range():
    assert arrs.my_slice([1, 2, 3], start=1) == [2, 3]

def test_my_slice_no_arguments():
    assert arrs.my_slice([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_my_slice_negative_start():
    assert arrs.my_slice([1, 2, 3, 4], start=-2) == [3, 4]

def test_my_slice_negative_end():
    assert arrs.my_slice([1, 2, 3, 4], end=-1) == [1, 2, 3]

def test_my_slice_empty_array():
    assert arrs.my_slice([], start=0, end=2) == []

def test_my_slice_start_and_end_equal():
    assert arrs.my_slice([1, 2, 3, 4], start=1, end=1) == []

def test_my_slice_start_and_end_negative():
    assert arrs.my_slice([1, 2, 3, 4], start=-3, end=-1) == [2, 3]

def test_my_slice_start_and_end_beyond_length():
    assert arrs.my_slice([1, 2, 3, 4], start=10, end=15) == []

def test_my_slice_full_range_negative_start():
    assert arrs.my_slice([1, 2, 3, 4], start=-4, end=4) == [1, 2, 3, 4]

def test_my_slice_full_range_negative_end():
    assert arrs.my_slice([1, 2, 3, 4], start=0, end=-1) == [1, 2, 3]

def test_my_slice_full_range_negative_start_and_end():
    assert arrs.my_slice([1, 2, 3, 4], start=-4, end=-1) == [1, 2, 3]