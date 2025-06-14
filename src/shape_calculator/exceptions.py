"""Модуль с пользовательскими исключениями для библиотеки"""

class ShapeError(Exception):
    """Базовый класс для ошибок, связанных с фигурами"""
    pass

class InvalidDimensionsError(ShapeError):
    """Исключение при некорректных размерах фигуры (например, отрицательный радиус)"""
    pass

class InvalidTriangleError(ShapeError):
    """Исключение в случае, когда стороны не могут образовать треугольник"""
    pass