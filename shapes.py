"""Module to calculate area and perimeter for basic shapes"""


import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape.
        This is an abstract method that must be implemented by subclasses."""

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape.
        This is an abstract method that must be implemented by subclasses."""


class Square(Shape):
    """Class representing a square shape."""

    def __init__(self, side: float):
        self.side = side
        if self.side < 0:
            raise ValueError("Value is negative")

    def perimeter(self) -> float:
        return 4 * self.side

    def area(self) -> float:
        return self.side * self.side

    def __str__(self):
        return (f"Square with side {self.side}, "
                f"Perimeter: {self.perimeter()}, Area: {self.area()}")


class Rectangle(Shape):
    """Class representing a rectangle shape."""

    def __init__(self, top_right_x: float, top_right_y: float,
                 bottom_left_x: float, bottom_left_y: float):
        self.top_right_x = top_right_x
        self.top_right_y = top_right_y
        self.bottom_left_x = bottom_left_x
        self.bottom_left_y = bottom_left_y
        self.width = abs(top_right_x - bottom_left_x)
        self.height = abs(top_right_y - bottom_left_y)

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def area(self) -> float:
        return self.width * self.height

    def __str__(self):
        return (f"Rectangle TopRight ({self.top_right_x}, {self.top_right_y}) "
                f"BottomLeft ({self.bottom_left_x}, {self.bottom_left_y}), "
                f"Perimeter: {self.perimeter()}, Area: {self.area()}")


class Circle(Shape):
    """Class representing a circle shape."""

    def __init__(self, radius: float):
        self.radius = radius

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def __str__(self):
        return (f"Circle with radius {self.radius},"
                f"Circumference: {self.perimeter()}, Area: {self.area()}")


class Triangle(Shape):
    """Class representing a triangle shape."""

    def __init__(self, x1: float, y1: float, x2: float, y2:
                 float, x3: float, y3: float):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3
        self.a = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        self.b = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        self.c = math.sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2)

    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def area(self) -> float:
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def __str__(self):
        return (f"Triangle with coordinates ({self.x1}, {self.y1}), "
                f"({self.x2}, {self.y2}), ({self.x3}, {self.y3}), "
                f"Perimeter: {self.perimeter()}, Area: {self.area()}")


def parse_input(input_line: str) -> Shape:
    """Parse an input string and return a Shape instance."""
    shape_constructors = {
        "Square": lambda elements: Square(float(elements[5])),
        "Rectangle": lambda elements: Rectangle(float(elements[2]), float(elements[3]), float(elements[5]), float(elements[6])),
        "Circle": lambda elements: Circle(float(elements[5])),
        "Triangle": lambda elements: Triangle(float(elements[2]), float(elements[3]),
                                              float(elements[5]), float(
                                                  elements[6]),
                                              float(elements[8]), float(elements[9]))
    }

    elements = input_line.split()
    shape_type = elements[0]

    if shape_type in shape_constructors:
        return shape_constructors[shape_type](elements)
    else:
        raise ValueError("The shape doesn't exist")


if __name__ == "__main__":
    user_input = input(
        "Please, enter shape and parameters (e.g., 'Circle Center 1 1 Radius 2'): ")
    shape = parse_input(user_input)
    print(shape)
