#!/usr/bin/python3
"""Square related feature module."""


class Square:
    """Class that define a Square."""

    def __init__(self, size=0, position=(0, 0)):
        """
            Args:
                size (int): size initializer
                position (tuple): a tuple of two position integer
        """

        self.size = size
        self.position = position

    def area(self):
        """Compute the area of the Square.

            Returns:
                The area. An (integer)
        """

        return (self.__size ** 2)

    @property
    def size(self):
        """__size property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """__size property setter.

            Args:
                value (int): new size value

            Raises:
                TypeError: if `value` is not an integer
                ValueError: if `value` is < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """__position proper getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """__position property setter"""
        if not (
                isinstance(value, tuple) and
                len(value) == 2 and
                isinstance(value[0], int) and
                isinstance(value[1], int) and
                value[0] >= 0 and
                value[1] >= 0):
            raise TypeError("position must be a tuple of 2 position integers")
        self.__position = value

    def my_print(self):
        """Draw the square to the stdout"""
        x = self.__position[0]
        y = self.__position[1]
        for _ in range(y):
            print()
        if self.__size == 0:
            print(" " * x)
            return

        for i in range(self.__size):
            print(" " * x + "#" * self.__size)
