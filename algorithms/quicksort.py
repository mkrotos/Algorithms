from typing import List


def quicksort(array: List) -> List:
    """
    Fast sorting algorithm

    :param array: list to be sorted
    :return: sorted list
    """
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([2, 6, 43, 7, 3]))
