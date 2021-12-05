from pybook.ch13.CircleWithCustomException import Circle
from pybook.ch13.InvalidRadiusException import InvalidRadiusException

try:
    c1 = Circle(5)
    print("cl-s area is", c1.getArea())
    c2 = Circle(-5)
    print("c2's area is", c2.getArea())
    c3 = Circle(0)
    print("c3's area is", c3.getArea())
except InvalidRadiusException as ex:
    print("The radius", ex.radius, "is invalid")
except Exception:
    print("Something is wrong")
