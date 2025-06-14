"""Модуль, содержащий фабрику для создания объектов фигур"""

from .shapes.base_shape import Shape
from .shapes.circle import Circle
from .shapes.triangle import Triangle
from .utils.logger import logger

# Словарь для сопоставления имен фигур с их классами
# Легко расширять, добавив новую пару "имя": Класс
SHAPE_REGISTRY = {
    "circle": Circle,
    "triangle": Triangle,
}


def create_shape(shape_type: str, *args, **kwargs) -> Shape:
    """
    Фабричная функция для создания объектов фигур по их типу.
    Args:
        shape_type (str): Тип фигуры (например, 'circle', 'triangle').
        *args, **kwargs: Аргументы для конструктора фигуры.
    Returns:
        Shape: Экземпляр соответствующего класса фигуры.
    Raises:
        ValueError: если тип фигуры не найден в реестре
    """
    shape_class = SHAPE_REGISTRY.get(shape_type.lower())
    if not shape_class:
        msg = f"Unknown type of figure: '{shape_type}'. Available types: {list(SHAPE_REGISTRY.keys())}"
        logger.error(msg)
        raise ValueError(msg)

    logger.info(f"The factory creates a shape like '{shape_type}'")
    return shape_class(*args, **kwargs)