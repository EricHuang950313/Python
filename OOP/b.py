import math

class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    def get_area(self):
        return math.pi * self._radius * self._radius

    def get_perimeter(self):
        return 2 * math.pi * self._radius

c1 = Circle(3)
print("radius:", "{:.2f}".format(c1.get_radius()))
print("area:", "{:.2f}".format(c1.get_area()))
print("perimeter:", "{:.2f}".format(c1.get_perimeter()))

c2 = Circle(5)
c2.set_radius(7)
print("radius:", "{:.2f}".format(c2.get_radius()))
print("area:", "{:.2f}".format(c2.get_area()))
print("perimeter:", "{:.2f}".format(c2.get_perimeter()))