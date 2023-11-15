"""Mutating points in a program using classes."""

from __future__ import annotations

__author__ = "730658668"


class Point:
    """Class representing a point in a program."""

    def __init__(self, init_x: float = 0.0, init_y: float = 0.0):
        """Create a Point instance from a given x and y coordinates."""
        self.x = init_x
        self.y = init_y

    def scale_by(self, factor: int) -> None:
        """Scale by the given factor and return the result."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: int) -> Point:
        """Scale by the given factor and return the result."""
        return Point(self.x * factor, self.y * factor)
    
    def __str__(self) -> str:
        """Return a string representation of this Point."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point:
        """Multiply point by factor."""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, add: int | float) -> Point:
        """Add a value to the point."""
        return Point(self.x + add, self.y + add)