from pybook.ch12.GeometricObject import GeometricObject


class Rectangle(GeometricObject):
    def __init__(self, width=1, height=1):
        super().__init__()
        self.__width = width
        self.__height = height

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width

    def getheight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height

    def getArea(self):
        return self.__height * self.__width

    def getPrimeter(self):
        return (self.__width + self.__height) * 2

    def __str__(self):
        return super().__str__() + " width: " + \
               str(self.__width) + " height: " + str(self.__height)
