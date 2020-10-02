from typing import List


def binary_search(target, array: List):
    """
    Find index of the target in sorted list (array) using binary search algorithm

    :param target: target number which index we want to find
    :param array: List of numbers
    """
    bottom = 0
    top = len(array) - 1

    counter = 0

    while counter < 20:
        counter += 1
        mid = int((bottom + top) / 2)

        if target == array[mid]:
            return mid
        elif target > array[mid]:
            bottom = mid
        else:
            top = mid

    return None
