import sys
import os
import math
from typing import List
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from c02.sorting import sort
import time
import logging

methods = ["python", "incremental", "inefficient_merge", "efficient_merge"]

@pytest.mark.parametrize("method", methods)
def test_sorting_empty(method):
    assert sort([], method) == []

@pytest.mark.parametrize("method", methods)
def test_sorting_single_element(method):
    assert sort([5], method) == [5]

@pytest.mark.parametrize("method", methods)
def test_sorting_basic(method):
    assert sort([3, 1, 2], method) == [1, 2, 3]
    assert sort([3, 3, 3], method) == [3, 3, 3]
    assert sort([2, 1, 3], method) == [1, 2, 3]
    assert sort([3, 2, 1], method) == [1, 2, 3]
    assert sort([1, 3, 2], method) == [1, 2, 3]
    assert sort([2, 3, 1], method) == [1, 2, 3]
    assert sort([1, 2, 3, 4, 5], method) == [1, 2, 3, 4, 5]
    assert sort([5, 4, 3, 2, 1], method) == [1, 2, 3, 4, 5]

@pytest.mark.parametrize("method", methods)
def test_sorting_runtime(method, caplog):
    caplog.set_level(logging.INFO)
    sizes = [100, 1_000, 10_000, 20_000]
    times = []

    for size in sizes:
        large_list = list(range(size, 0, -1))  # Reverse sorted list
        start_time = time.time()
        sort(large_list, method)
        end_time = time.time()
        runtime = end_time - start_time
        times.append(runtime)
        log_message = f"Runtime for {method} with {size} elements: {runtime:.6f} seconds"
        logging.info(log_message)
        print(log_message)

    complexity = estimate_complexity(sizes, times)
    log_message = f"Estimated complexity for {method}: {complexity}"
    logging.info(log_message)
    print(log_message)

    assert all(t > 0 for t in times)  # Ensure all runtimes are positive

def estimate_complexity(sizes: List[int], times: List[float]) -> str:
    log_sizes = [math.log(size) for size in sizes]
    log_times = [math.log(time) for time in times]
    
    n = len(sizes)
    slope = (n * sum(x*y for x, y in zip(log_sizes, log_times)) - sum(log_sizes) * sum(log_times)) / \
            (n * sum(x*x for x in log_sizes) - sum(log_sizes)**2)
    
    if slope < 1.2:
        return "O(n)" if slope > 0.8 else "O(log n) or better"
    elif slope < 1.8:
        return "O(n log n)"
    else:
        return "O(n^2) or worse"
