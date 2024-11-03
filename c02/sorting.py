def incremental_sort(array):
    """
    runtime: O(n^2)
    space: O(n)
    """
    for i in range(1, len(array)): # O(n)
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key: # b/w O(1) and O(n) (worst case)
            array[j+1] = array[j] # keeping list intact so space is O(n)
            j -= 1
        array[j+1] = key
    return array

def inefficient_merge_sort(array): # idk what @cache does to memory here
    """
    runtime: O(log(n)n^2) apparently
    space: ?
    """
    array_len = len(array)
    
    # base case
    if array_len <= 1:
        return array
    # one interesting possibility here would be to switch to incremental_sort whenever
    # the leaves are sufficiently small

    # recursion
    bi = array_len//2
    array1 = inefficient_merge_sort(array[:bi]) # recursive dividing by 2 gives us O(nlog_2(n))
    array2 = inefficient_merge_sort(array[bi:])
    new_array = []
    while len(array1) > 0 or len(array2) > 0: # each of these loops is itself O(n)
        try:
            if array1[0] <= array2[0]:
                new_array.append(array1.pop(0))
            else:
                new_array.append(array2.pop(0))
        except IndexError:
            if len(array1) == 0:
                new_array.append(array2.pop(0))
            elif len(array2) == 0:
                new_array.append(array1.pop(0))
            else:
                raise IndexError()
    return new_array

def merge_tool(array, p, q, r):
    """
    runtime: O(n)
    space: O(n)
    """
    l1 = q - p
    l2 = r - q
    a1 = [array[p + i] for i in range(l1)]
    a2 = [array[q + i] for i in range(l2)]

    i, j = 0, 0
    for k in range(p, r):
        if i < l1 and (j >= l2 or a1[i] <= a2[j]):
            array[k] = a1[i]
            i += 1
        else:
            array[k] = a2[j]
            j += 1

    return array

def efficient_merge_sort(array, p = 0, r = None):
    """
    runtime: O(nlog(n))
    space: ?
    """
    # correct init values
    r = len(array) if r == None else r

    array_len = len(array[p:r])

    # base case
    if array_len <= 1:
        return array
    
    if p < r:
        q = (p + r) // 2
        array = efficient_merge_sort(array, p, q)
        array = efficient_merge_sort(array, q, r)
        return merge_tool(array, p, q, r)
    else:
        return array
    
            
def python_sort(array):
    return sorted(array)

def sort(array: list, method: str):
    key = {
        'incremental': incremental_sort, 
        'inefficient_merge': inefficient_merge_sort, 
        'efficient_merge': efficient_merge_sort,
        'python': python_sort,
    }
    if method in key:
        return key[method](array)
    
