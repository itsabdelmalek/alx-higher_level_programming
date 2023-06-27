#!/usr/bin/python3

"""
This module defines a square
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a square with the given size.

        Args:
            size: The size of the square (optional, default is 0).

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value: The size of the square.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if the area of the current square is = the area of other square

        Args:
            other: The other square to compare with.

        Returns:
            True if the areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """
        Checks if the area of the current square != to the area of other square

        Args:
            other: The other square to compare with.

        Returns:
            True if the areas are not equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __gt__(self, other):
        """
        Checks if the area of the current square is > the area of other square.

        Args:
            other: The other square to compare with.

        Returns:
            True if the area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Checks if the area of the current square is >= the area of other square

        Args:
            other: The other square to compare with.

        Returns:
            True if the area is greater than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """
        Checks if the area of the current square is <  the area of other square

        Args:
            other: The other square to compare with.

        Returns:
            True if the area is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Checks if the area of the current square is <= another square

        Args:
            other: The other square to compare with.

        Returns:
            True if the area is less than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area
