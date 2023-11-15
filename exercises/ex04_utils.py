"""EX04 - Using lists in functions."""

__author__ = 730658668


def all(list: list[int], value: int) -> bool:
    """Check if all elements in the list are equal to the given value."""
    if len(list) == 0:
        return False
    list_idx: int = 0
    list_len: int = len(list)
    while list_idx < list_len:
        if list[list_idx] != value:
            return False
        list_idx += 1
    return True


def max(input: list[int]) -> int:
    """Return the maximum value from the list or return error if the list is empty."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    list_idx: int = 1
    list_len: int = len(input)
    max_value: int = input[0]
    while list_idx < list_len:
        if input[list_idx] > max_value:
            max_value = input[list_idx]
        else:
            list_idx += 1
        list_idx += 1
    return max_value


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Check if two lists are equal."""
    if len(list1) == 0 and len(list2) == 0:
        return True
    if len(list1) != len(list2):
        return False
    list_idx: int = 0
    list1_len: int = len(list1)
    list2_len: int = len(list2)
    while list_idx < list1_len and list_idx < list2_len:
        if list1[list_idx] != list2[list_idx]:
            return False
        list_idx += 1
    return True