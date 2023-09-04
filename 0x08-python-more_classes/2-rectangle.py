#!/usr/bin/python3
"""0-rectangle.py : Rectangle class"""


class Rectangle:
    """
    A class that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """The constructor

        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = width
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = height
        else:
            raise TypeError("height must be an integer")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Getter for the width

        Returns:
            int : the width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for the width

        Args:
            width (int): width of the rectangle.

        Raises:
            TypeError: if width not an integer
            ValueError: if width < 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Getter for the height

        Returns:
            int : the height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for the height

        Args:
            height (int): height of the rectangle.

        Raises:
            TypeError: if height not an integer
            ValueError: if height < 0
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """
        Returns:
            int: The rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns:
            int: The rectangle perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2
