"""Модуль, содержащий класс для представления треугольника"""

import math
from .base_shape import Shape
from ..exceptions import InvalidDimensionsError, InvalidTriangleError
from ..utils.logger import logger


class Triangle(Shape):
    """Класс для представления треугольника и вычисления его площади"""
    def __init__(self, a: float, b: float, c: float):
        """
        Инициализирует объект треугольника.
        Args:
            a (float): Длина стороны a
            b (float): Длина стороны b
            c (float): Длина стороны c
        Raises:
            InvalidDimensionsError: если любая из сторон меньше или равна нулю.
            InvalidTriangleError: если стороны не удовлетворяют неравенству треугольника.
        """
        sides = [a, b, c]
        if not all(side > 0 for side in sides):
            msg = f"The lengths of the sides of the triangle must be positive, it is obtained: {sides}"
            logger.error(msg)
            raise InvalidDimensionsError(msg)

        sides.sort()
        if sides[0] + sides[1] <= sides[2]:
            msg = f"The sides {sides} cannot form a triangle (triangle inequality is violated)."
            logger.error(msg)
            raise InvalidTriangleError(msg)

        self.a, self.b, self.c = a, b, c
        logger.info(f"A Triangle object with sides has been created({self.a}, {self.b}, {self.c})")

    def area(self) -> float:
        """
        Вычисляет площадь треугольника по формуле Герона.
        Returns:
            float: Площадь треугольника
        """
        s = (self.a + self.b + self.c) / 2  # Полупериметр
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        logger.info(f"Calculated the area for Triangle(a={self.a}, b={self.b}, c={self.c}): {area}")
        return area

    def is_right_angled(self) -> bool:
        """
        Проверяет, является ли треугольник прямоугольным.
        Проверка выполняется с использованием теоремы Пифагора с учетом
        возможной погрешности вычислений с плавающей точкой.
        Returns:
            bool: True, если треугольник прямоугольный, иначе False.
        """
        sides = sorted([self.a, self.b, self.c])
        # Используем math.isclose для безопасного сравнения float
        is_right = math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
        logger.info(f"Checking for squareness for Triangle({self.a}, {self.b}, {self.c}): {is_right}")
        return is_right