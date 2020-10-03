from typing import List


def binary_search(list: List, item):
    """
    Find index of the item in sorted list using binary search algorithm

    :param item: item (number) which index we want to find
    :param list: List of numbers
    """
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


example_list = [1, 3, 4, 6, 8]

item = 3
print(f'Index of {item} is {binary_search(example_list, item)}')  # returns 1
item = -1
print(f'Index of {item} is {binary_search(example_list, item)}')  # returns None
