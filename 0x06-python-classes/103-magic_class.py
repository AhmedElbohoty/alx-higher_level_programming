#!/usr/bin/python3
""" Create Magic class """
import math


class MagicClass:
    """ Create circle
    """
    def __init__(self, radius=0):
        """ Init circle

            Args:
                radius (int): circle radius

            Raises:
                TypeError: radius must be a number
        """
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ Calculates circle are
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ Calculates circle circumference
        """
        return 2 * math.pi * self.__radius
