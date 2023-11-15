"""Combining two lists into a dictionary."""


__author__ = "730658668"


def zip(x: list[str], y: list[int]) -> dict[str, int]:
    """Combining two lists into a dictionary."""
    if len(x) != len(y):
        print("Lists are not of the same length")
        return {}
    z: dict[str, int] = {}
    i: int = 0
    while i < len(x):
        z[x[i]] = y[i]
        i += 1
    return z
        