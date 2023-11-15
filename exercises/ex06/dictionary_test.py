"""Creating test cases for dictionary functions."""

__author__ = 730658668

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_two_keys() -> None:
    """Test invert with two keys."""
    x: dict[str, str] = {"a": "b", "c": "d"}
    assert invert(x) == {"b": "a", "d": "c"}
    
    
def test_invert_same_value() -> None:
    """Test invert with two keys and one value."""
    x: dict[str, str] = {"a": "b", "c": "b"}
    assert invert(x) == {"b": "c"}


def test_invert_empty_dict() -> None:
    """Test invert with an empty dictionary."""
    x: dict[str, str] = {}
    assert invert(x) == {}


def test_favorite_color_one_color() -> None:
    """Test favorite_color with one color."""
    x: dict[str, str] = {"a": "b"}
    assert favorite_color(x) == "b"


def test_favorite_color_two_color() -> None:
    """Test favorite_color with two colors."""
    x: dict[str, str] = {"a": "b", "c": "b"}
    assert favorite_color(x) == "b"


def test_favorite_color_no_colors() -> None:
    """Test favorite_color with no colors."""
    x: dict[str, str] = {}
    assert favorite_color(x) == "No favorite color."


def test_count_one_string() -> None:
    """Test count with one string."""
    x: list[str] = ["a"]
    assert count(x) == {"a": 1}


def test_count_two_strings() -> None:
    """Test count with two strings."""
    x: list[str] = ["a", "b"]
    assert count(x) == {"a": 1, "b": 1}


def test_count_no_string() -> None:
    """Test count with no strings."""
    x: list[str] = []
    assert count(x) == {}


def test_alphabetizer_two_strings_different_cases() -> None:
    """Test alphabetizer with strings of different cases."""
    x: list[str] = ["jogging", "citrus", "circus", "Circus", "Jolly"]
    assert alphabetizer(x) == {"j": ["jogging", "Jolly"], "c": ["citrus", "circus", "Circus"]}


def test_alphabetizer_two_strings() -> None:
    """Test alphabetizer with two strings."""
    x: list[str] = ["alpha", "beta"]
    assert alphabetizer(x) == {"a": ["alpha"], "b": ["beta"]}


def test_alphabetizer_no_strings() -> None:
    """Test alphabetizer with no strings."""
    x: list[str] = []
    assert alphabetizer(x) == {}


def test_update_attendance_same_name_two_days() -> None:
    """Test update_attendance with the same name on two different days."""
    x: dict[str, list[str]] = {"Monday": ["Anna"], "Tuesday": ["Anna"]}
    x = update_attendance(x, "Monday", "Anna")
    x = update_attendance(x, "Tuesday", "Anna")
    expected: dict[str, list[str]] = {"Monday": ["Anna"], "Tuesday": ["Anna"]}
    assert x == expected


def test_update_attendance_three_day_four_students() -> None:
    """Test update_attendance with three days and four students."""
    x: dict[str, list[str]] = {"a": ["b"], "c": ["d"], "e": ["f"]}
    assert update_attendance(x, "a", "g") == {"a": ["b", "g"], "c": ["d"], "e": ["f"]}


def test_update_attendance_no_students_no_days() -> None:
    """Test update_attendance with no students and no days."""
    x: dict[str, list[str]] = {}
    assert update_attendance(x, "a", "b") == {"a": ["b"]}
