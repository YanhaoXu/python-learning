import math

from pybook.ch12.GeometricObject import GeometricObject
from pybook.ch13.InvalidRadiusException import InvalidRadiusException


class Circle(GeometricObject):
    def __init__(self, radius):
        super().__init__()
        self.setRadius(radius)

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        if radius >= 0:
            self.__radius = radius
        else:
            raise InvalidRadiusException(radius)

    def getArea(self):
        return self.__radius ** 2 * math.pi

    def getDiameter(self):
        return 2 * self.__radius

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def printCircle(self):
        print(self.__str__(), "radius:", self.__radius)
