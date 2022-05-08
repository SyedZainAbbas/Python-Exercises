"""
EXERCISE: Circle
Create an Circle class that has one instance variable named “radius”.
Add a method to calculate and print the area of the circle.
The area of a circle is calculated by multiplying Pi by the square of the radius: Pi x r2
Rework the Circle class so that the area is calculated during initialization and stored in an “area” attribute.

"""

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)


first = Circle(5)
print('Circle:', first.area())


class ReworkCircle:
    def __init__(self, radius):
        self.radius = radius
        self.area = round(radius ** 2 * math.pi, 2)


second = ReworkCircle(5)
print('Reworked Circle:', second.area)
