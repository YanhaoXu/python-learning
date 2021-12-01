import math

from GeometricObject import GeometricObject


class Circle(GeometricObject):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, raidus):
        self.__radius = raidus

    def getArea(self):
        return math.pi * self.__radius ** 2

    def getDiameter(self):
        return self.__radius * 2

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def printCircle(self):
        print(self.__str__() + " radius: " + str(self.__radius))

    def __str__(self):
        return super().__str__() + " radius: " + str(self.__radius)
