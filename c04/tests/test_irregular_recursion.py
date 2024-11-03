# finding the maximum subarray result_sum
import sys
import os
import math
from typing import List
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from c04.irregular_recursion import max_subarray_sum_recursion
from c04.iterator import max_subarray_sum_iterator

@pytest.mark.parametrize("max_subarray_func", [
    max_subarray_sum_recursion,
    max_subarray_sum_iterator
])
def test_empty_array(max_subarray_func):
    with pytest.raises(ValueError):
        max_subarray_func([])

@pytest.mark.parametrize("max_subarray_func", [
    max_subarray_sum_recursion,
    max_subarray_sum_iterator
])
def test_large_array(max_subarray_func):
    large_array = [i % 5 - 2 for i in range(10000)]
    low, high, result_sum = max_subarray_func(large_array)
    assert result_sum > 0
    assert high > low

@pytest.mark.parametrize("max_subarray_func", [
    max_subarray_sum_recursion,
    max_subarray_sum_iterator
])
def test_all_negative(max_subarray_func):
    input_array = [-1, -2, -3, -4, -5]
    low, high, result_sum = max_subarray_func(input_array)
    assert result_sum == -1
    assert (low, high) == (0, 0)

@pytest.mark.parametrize("max_subarray_func", [
    max_subarray_sum_recursion,
    max_subarray_sum_iterator
])
@pytest.mark.parametrize("input_array, expected_sum, expected_indices", [
    ([1, -3, 2, 1, -1], 3, (2, 3)),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6, (3, 6)),
    ([5, 4, -1, 7, 8], 23, (0, 4)),
    ([-1, -2, -3, -4], -1, (0, 0)),
    ([1], 1, (0, 0)),
    ([-1, 2, 3, -4, 5, -6], 6, (1, 4)),
])
def test_max_subarray_sum(max_subarray_func, input_array, expected_sum, expected_indices):
    low, high, result_sum = max_subarray_func(input_array)
    assert result_sum == expected_sum, f"Expected sum {expected_sum}, but got {result_sum}"
    assert (low, high) == expected_indices, f"Expected indices {expected_indices}, but got {(low, high)}"
