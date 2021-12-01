from pybook.ch12.CircleFromGeometicObject import Circle
from pybook.ch12.ReatangleFromGeometricObject import Rectangle


def main():
    circle = Circle(1.5)
    print("A circle", circle)
    print("The radius is", circle.getRadius())
    print("The area is", circle.getArea())
    print("The diameter is", circle.getDiameter())

    rectangle = Rectangle(2, 4)
    print("\nA rectangle", rectangle)
    print("The area is", rectangle.getArea())
    print("The perimeter is", rectangle.getPrimeter())


main()
