from typing import List


def sum(arr: List) -> int:
    """
    Sums elements in list using recursive algorithm

    :param arr: list of numbers
    :return: sum
    """
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])


def count_elements_in_list(arr: List) -> int:
    """
    Counts number of elements in list using recursive algorithm

    :param arr: list of any elements
    :return: number of elements
    """
    if not arr:
        return 0
    else:
        return 1 + count_elements_in_list(arr[1:])


def find_max(arr: List) -> int:
    """
    Finds max number in the list using recursive algorithm

    :param arr: list of numbers
    :return: max element
    """
    return _find_max_recursion_case(arr, 0)


def _find_max_recursion_case(arr: List, max: int) -> int:
    if not arr:
        return max
    else:
        return _find_max_recursion_case(arr[1:], arr[0])
