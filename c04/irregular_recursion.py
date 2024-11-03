# finding the maximum subarray sum
# using divide and conquer recursion with an irregular sub-task

def _max_crossing_subarray(array, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    for i in range(mid, low-1, -1):
        sum += array[i]
        if sum > left_sum:
            low = i
            left_sum = sum
    right_sum = float('-inf')
    sum = 0
    for i in range(mid+1, high):
        sum += array[i]
        if sum > right_sum:
            high = i
            right_sum = sum
    return low, high, left_sum + right_sum

def max_subarray_sum_recursion(array, low = 0, high = None): # O(nlog(n))
    high = len(array) if high is None else high
    if high == 0: raise ValueError
    # base case
    if low >= high-1:
        return low, low, array[low] if low < high else 0
    
    bi = low + (high - low)//2
    left_low, left_high, left_sum = max_subarray_sum_recursion(array, low, bi)
    right_low, right_high, right_sum = max_subarray_sum_recursion(array, bi, high)
    cross_low, cross_high, cross_sum = _max_crossing_subarray(array, low, bi, high)

    if (left_sum > right_sum) and (left_sum > cross_sum):
        return left_low, left_high, left_sum
    elif (right_sum > left_sum) and (right_sum > cross_sum):
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum

        

