"""Модуль, содержащий класс для представления круга"""

import math
from .base_shape import Shape
from ..exceptions import InvalidDimensionsError
from ..utils.logger import logger


class Circle(Shape):
    """Класс для представления круга и вычисления его площади"""
    def __init__(self, radius: float):
        """
        Инициализирует объект круга.
        Args:
            radius (float): Радиус круга.
        Raises:
            InvalidDimensionsError: если радиус меньше или равен нулю
        """
        if radius <= 0:
            msg = f"The radius must be a positive number, obtained by: {radius}"
            logger.error(msg)
            raise InvalidDimensionsError(msg)

        self.radius = radius
        logger.info(f"A Circle object with a radius has been created {self.radius}")

    def area(self) -> float:
        """
        Вычисляет площадь круга по формуле π * r^2.
        Returns:
            float: Площадь круга.
        """
        area = math.pi * self.radius ** 2
        logger.info(f"Calculated the area for Circle(radius={self.radius}): {area}")
        return area