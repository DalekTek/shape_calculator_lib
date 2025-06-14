"""
Shape Calculator Library
========================

Публичный API библиотеки для вычисления площади фигур.
"""

# Делаем основные классы и функции доступными для импорта напрямую из пакета
from .shapes.base_shape import Shape
from .shapes.circle import Circle
from .shapes.triangle import Triangle
from .factory import create_shape
from .exceptions import ShapeError, InvalidDimensionsError, InvalidTriangleError

# Определяем, что будет экспортироваться при 'from shape_calculator import *'
__all__ = [
    "Shape",
    "Circle",
    "Triangle",
    "create_shape",
    "ShapeError",
    "InvalidDimensionsError",
    "InvalidTriangleError",
]