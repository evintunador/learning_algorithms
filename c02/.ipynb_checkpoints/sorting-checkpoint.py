def incremental_sort(array):
    for i in range(1, len(array)): # O(n)
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key: # b/w O(1) and O(n) (worst case)
            array[j+1] = array[j] # keeping list intact so space is O(n)
            j -= 1
        array[j+1] = key
    return array
# runtime: O(n^2)
# space: O(n)

@cache # might help runtime a tiny bit in specific scenario of repeated sub-sequences
def merge_sort(array): # idk what @cache does to memory here
    array_len = len(array)
    
    # base case
    if array_len <= 1:
        return array
    # one interesting possibility here would be to switch to incremental_sort whenever
    # the leaves are sufficiently small

    # recursion
    bi = array_len//2
    array1 = merge_sort(array[:bi]) # recursive dividing by 2 gives us O(nlog_2(n))
    array2 = merge_sort(array[bi:])
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
            
def python_sort(array):
    return sorted(array)

def sort(array: list, method: str):
    key = {
        'incremental': incremental_sort, 
        'merge': merge_sort, 
        'python': python_sort,
    }
    if method in key:
        return key[method](array)
    
