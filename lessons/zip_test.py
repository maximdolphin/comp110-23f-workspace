"""Test my zip function."""

__author__ = "730658668"

from lessons.zip import zip


def test_two_lists_same_length() -> None:
    """Test zip with two lists of the same length."""
    x: list[str] = ["a", "b", "c"]
    y: list[int] = [1, 2, 3]
    assert zip(x, y) == {"a": 1, "b": 2, "c": 3}
    

def test_two_lists_different_length() -> None:
    """Test zip with two lists of different length."""
    x: list[str] = ["a", "b", "c"]
    y: list[int] = [1, 2]
    assert zip(x, y) == {}
    

def test_same_values_diff_keys() -> None:
    """Test zip with two values being the same but all keys different."""
    x: list[str] = ["Apples", "Oranges", "Pears"]
    y: list[int] = [1, 3, 3]
    assert zip(x, y) == {"Apples": 1, "Oranges": 3, "Pears": 3}
    