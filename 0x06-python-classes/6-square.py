#!/usr/bin/python3

""" This module defines the Square class. """


class Square:
    """This class represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size (int, size): The size of the square. Defaults to 0.
                        position (tuple, optional): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
                        TypeError: If the position is not a tuple of 2 positive integers.
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If the position is not a tuple of 2 positive integers.
            ValueError: If the position contains negative integers.

        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(coord, int) for coord in value)
            or not all(coord >= 0 for coord in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Computes the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size**2

    def my_print(self):
        """
        Prints the square using the character '#'.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
