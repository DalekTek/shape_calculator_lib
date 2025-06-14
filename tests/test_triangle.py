import pytest
import math
from src.shape_calculator import Triangle
from src.shape_calculator.exceptions import InvalidDimensionsError, InvalidTriangleError

def test_right_angled_triangle():
    """Тест для прямоугольного треугольника"""
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0)
    assert t.is_right_angled() is True

def test_equilateral_triangle():
    """Тест для равностороннего треугольника"""
    t = Triangle(5, 5, 5)
    expected_area = (math.sqrt(3) / 4) * 5**2
    assert math.isclose(t.area(), expected_area)
    assert t.is_right_angled() is False

def test_invalid_dimensions():
    """Тест создания треугольника с некорректными сторонами"""
    with pytest.raises(InvalidDimensionsError):
        Triangle(3, 4, -5)
    with pytest.raises(InvalidDimensionsError):
        Triangle(3, 0, 5)

def test_triangle_inequality_error():
    """Тест на нарушение неравенства треугольника"""
    with pytest.raises(InvalidTriangleError, match="triangle inequality is violated"):
        Triangle(1, 2, 5)

def test_is_right_angled_with_floats():
    """Тест проверки на прямоугольность для float-значений"""
    # sqrt(2)^2 + sqrt(3)^2 = 5, sqrt(5)^2 = 5
    t = Triangle(math.sqrt(2), math.sqrt(3), math.sqrt(5))
    assert t.is_right_angled() is True