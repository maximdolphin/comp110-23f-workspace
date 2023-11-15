"""Summing the elements of a list using different loops."""

__author__ = 730658668


def w_sum(vals: list[float]) -> float:
    """Input a list of floats and return the sum of all elements in the list using a while loop."""
    list_len: float = len(vals)
    list_idx = 0
    result: float = 0
    while list_idx < list_len:
        result += vals[list_idx]
        list_idx += 1
        
    return result


def f_sum(vals: list[float]) -> float:
    """Input a list of floats and return the sum of all elements in the list using a for loop."""
    result: float = 0
    for val in vals:
        result += val
        
    return result


def f_range_sum(vals: list[float]) -> float:
    """Input a list of floats and return the sum of all elements in the list across a range using a for loop."""
    result: float = 0
    for idx in range(0, len(vals)):
        result += vals[idx]
        
    return result


