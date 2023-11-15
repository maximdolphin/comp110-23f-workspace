"""Creating multiple functions modifying dictionaries in various ways."""

__author__ = "7303658668"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Return a new dictionary with keys and values inverted."""
    output: dict[str, str] = {}
    for key in x:
        output[x[key]] = key
    return output


def favorite_color(x: dict[str, str]) -> str:
    """Determine the most frequent color in a dictionary mapping names to favorite colors."""
    if x == {}:
        return "No favorite color."
    output: dict[str, int] = {}
    for key in x:
        if x[key] in output:
            output[x[key]] += 1
        else:
            output[x[key]] = 1
    max_value = max(output.values())
    for key in output:
        if output[key] == max_value:
            return key
    return "No favorite color."


def count(x: list[str]) -> dict[str, int]:
    """Count the occurrence of each string in a list."""
    output: dict[str, int] = {}
    for key in x:
        if key in output:
            output[key] += 1
        else:
            output[key] = 1
    return output


def alphabetizer(x: list[str]) -> dict[str, list[str]]:
    """Organize a list of strings into a dictionary keyed by their first character."""
    output: dict[str, list[str]] = {}
    for item in x:
        key = item[0].lower()
        if key in output:
            output[key].append(item)
        else:
            output[key] = [item]
    return output


def update_attendance(x: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Add a student's name to the attendance list for a given day."""
    if day in x:
        if student not in x[day]:
            x[day].append(student)
    else:
        x[day] = [student]
    return x
