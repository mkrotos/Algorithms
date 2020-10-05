from typing import List


def _find_smallest(arr: List) -> int:
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: List) -> List:
    """
    Returns new sorted list using selection sort algorithm

    :param arr: List to be sorted
    :returns: sorted list
    """
    new_arr = []
    for i in range(len(arr)):
        smallest = _find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort([1, 7, 2, 3, 8, 1]))
print(selection_sort(['a', 'g', 'c']))
