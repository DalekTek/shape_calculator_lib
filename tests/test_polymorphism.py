"""Тест, демонстрирующий полиморфное вычисление площади"""

import math
from src.shape_calculator import Shape, Circle, Triangle

def calculate_total_area(shapes: list[Shape]) -> float:
    """Функция, вычисляющая общую площадь списка фигур без знания их типов"""
    return sum(s.area() for s in shapes)

def test_area_calculation_without_knowing_type():
    """Проверяет, что можно вычислить площадь, не зная конкретный тип фигуры"""
    shapes: list[Shape] = [
        Circle(1),                  # Площадь = pi
        Triangle(3, 4, 5), # Площадь = 6
        Circle(2),                  # Площадь = 4*pi
    ]

    expected_total_area = math.pi * 1**2 + 6.0 + math.pi * 2**2
    total_area = calculate_total_area(shapes)

    assert math.isclose(total_area, expected_total_area)