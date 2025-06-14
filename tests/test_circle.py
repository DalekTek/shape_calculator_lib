import pytest
import math
from src.shape_calculator import Circle
from src.shape_calculator.exceptions import InvalidDimensionsError

def test_circle_creation_and_area():
    """Тест успешного создания круга и вычисления его площади"""
    c = Circle(10)
    assert c.radius == 10
    assert math.isclose(c.area(), math.pi * 100)

def test_circle_creation_with_zero_radius():
    """Тест создания круга с нулевым радиусом (с ошибкой)"""
    with pytest.raises(InvalidDimensionsError):
        Circle(0)

def test_circle_creation_with_negative_radius():
    """Тест создания круга с отрицательным радиусом (с ошибкой)"""
    with pytest.raises(InvalidDimensionsError, match=f"The radius must be a positive number"):
        Circle(-5)