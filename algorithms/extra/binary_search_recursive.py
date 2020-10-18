from typing import List


def binary_search_recursive(list: List, item):
    """
    Find index of the item in sorted list using recursive binary search algorithm

    :param item: item (number) which index we want to find
    :param list: List of numbers
    """
    low = 0
    high = len(list) - 1
    return _binary_search_recursive(list, item, low, high)


def _binary_search_recursive(list: List, item, low, high):
    mid = int((low + high) / 2)
    guess = list[mid]

    if low > high:
        return None

    if guess == item:
        return mid
    elif guess > item:
        high = mid - 1
        return _binary_search_recursive(list, item, low, high)
    else:
        low = mid + 1
        return _binary_search_recursive(list, item, low, high)


example_list = [1, 3, 4, 6, 8]

item = 3
print(f'Index of {item} is {binary_search_recursive(example_list, item)}')  # returns 1
item = -1
print(f'Index of {item} is {binary_search_recursive(example_list, item)}')  # returns None
