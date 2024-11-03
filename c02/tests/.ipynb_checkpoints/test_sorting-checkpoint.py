import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from chap_02.sorting import sort

@pytest.mark.parametrize("method", ["python", "incremental", "merge"])
def test_sorting_empty(method):
    assert sort([], method) == []

@pytest.mark.parametrize("method", ["python", "incremental", "merge"])
def test_sorting_single_element(method):
    assert sort([5], method) == [5]

@pytest.mark.parametrize("method", ["python", "incremental", "merge"])
def test_sorting_basic(method):
    assert sort([3, 1, 2], method) == [1, 2, 3]
    assert sort([3, 3, 3], method) == [3, 3, 3]
    assert sort([2, 1, 3], method) == [1, 2, 3]
    assert sort([3, 2, 1], method) == [1, 2, 3]
    assert sort([1, 3, 2], method) == [1, 2, 3]
    assert sort([2, 3, 1], method) == [1, 2, 3]
    assert sort([1, 2, 3, 4, 5], method) == [1, 2, 3, 4, 5]
    assert sort([5, 4, 3, 2, 1], method) == [1, 2, 3, 4, 5]