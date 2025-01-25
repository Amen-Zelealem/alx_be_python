import math

class Shape:
    """Base class representing a generic shape."""
    def area(self):
        """Method to be overridden in derived classes."""
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    """Derived class representing a rectangle."""
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return math.pi * self.radius ** 2
