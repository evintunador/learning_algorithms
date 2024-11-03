def max_subarray_sum_iterator(array):
    d = len(array)
    if d == 0:
        raise ValueError
    elif d == 1:
        return 0, 0, array[0]
    
    left = 0
    best_left = 0
    best_len = 1
    best_sum = 0
    for right in range(1,d):
        curr_sum = sum(array[left:right])
        if curr_sum > best_sum:
            best_sum = curr_sum
            best_left = left
            best_len = right - left