#!/usr/bin/python3
"""This is the ``Rectangle`` module"""


class Rectangle:
    """The Rectangle class defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize an instance of the Rectangle class.

            Args:
                width (int): The width of the rectangle
                height (int): The height of the rectangle
        """

        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the witdh of the rectangle"""

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the permeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle

            Args:
                rect_1 (Rectangle): an instance of Rectangle
                rect_2 (Rectangle): an instance of Rectangle

            Returns: The bigger Rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() - rect_2.area() >= 0 else rect_2

    def __str__(self):
        """Returns a string represenation of a rectangle"""
        text = ""
        w = self.__width
        h = self.__height

        if h == 0 or w == 0:
            return ""

        print_symbol = str(self.print_symbol)

        if h > 0:
            text = print_symbol * w
            h -= 1
        return text + ("\n" + print_symbol * w) * h

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when the rectange being deleted"""
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")
