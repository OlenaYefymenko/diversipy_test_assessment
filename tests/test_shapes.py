import pytest
from ..shapes import Square, Rectangle, Circle, Triangle, parse_input


@pytest.mark.parametrize(
    "input_str,expected_str,expected_type",
    [
        ("Square TopRight 1 1 Side 1",
         "Square with side 1.0, Perimeter: 4.0, Area: 1.0", Square),

        ("Rectangle TopRight 1 1 BottomLeft 2 2",
         "Rectangle TopRight (1.0, 1.0) BottomLeft (2.0, 2.0), Perimeter: 4.0, Area: 1.0", Rectangle),

        ("Circle Center 1 1 Radius 2",
         "Circle with radius 2.0,Circumference: 12.566370614359172, Area: 12.566370614359172", Circle),

        ("Triangle Point1 5 5 Point2 8 8 Point3 10 2",
         "Triangle with coordinates (5.0, 5.0), (8.0, 8.0), (10.0, 2.0), Perimeter: 16.398147902301346, Area: 12.000000000000005", Triangle),
    ]
)
def test_shape_parsing(input_str, expected_str, expected_type):
    shape = parse_input(input_str)
    assert isinstance(
        shape, expected_type), f"Expected type was {expected_type.__name__}, got {type(shape).__name__}"
    assert str(
        shape) == expected_str, f"Expected string was {expected_str}, got {str(shape)}"


def test_square_perimeter():
    a = Square(4)
    assert a.perimeter() == 16
    
def test_square_zero():
    x = Square(0)
    assert x.perimeter() == 0
    
def test_square_area():
    b = Square(2)
    assert b.area() == 4
    
def test_square_area_zero():
    b = Square(0)
    assert b.area() == 0
    
def test_square_perimeter_negative():
    with pytest.raises(ValueError):
        a = Square(-2)
    
    
def test_square_str():
    c = Square(2.0)
    assert str(c) == "Square with side 2.0, Perimeter: 8.0, Area: 4.0"
 
def test_square_str_zero():
    d = Square(0.0)
    assert str(d) == "Square with side 0.0, Perimeter: 0.0, Area: 0.0"  
