import pytest
from src.shape_calculator import create_shape, Circle, Triangle
from src.shape_calculator.exceptions import InvalidDimensionsError

def test_factory_create_circle():
    """Тест создания круга через фабрику"""
    shape = create_shape("circle", radius=5)
    assert isinstance(shape, Circle)
    assert shape.radius == 5

def test_factory_create_triangle():
    """Тест создания треугольника через фабрику"""
    shape = create_shape("triangle", 7, 8, 9)
    assert isinstance(shape, Triangle)
    assert shape.a == 7

def test_factory_case_insensitive():
    """Тест на нечувствительность к регистру в фабрике"""
    shape = create_shape("CiRcLe", radius=1)
    assert isinstance(shape, Circle)

def test_factory_unknown_shape():
    """Тест создания неизвестной фигуры"""
    with pytest.raises(ValueError, match="Unknown type of figure"):
        create_shape("hexagon", side=10)

def test_factory_invalid_args():
    """Тест передачи неверных аргументов через фабрику"""
    with pytest.raises(InvalidDimensionsError):
        create_shape("circle", radius=-1)