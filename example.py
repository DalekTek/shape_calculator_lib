"""
Пример использования библиотеки shape_calculator.

Этот скрипт демонстрирует:
1. Прямое создание объектов фигур (Круг, Треугольник).
2. Вычисление их площади.
3. Использование специфичных для фигуры методов (проверка на прямоугольность).
4. Обработку ошибок при создании фигур с некорректными данными.
5. Полиморфное использование фигур (вычисление площади без знания типа).
6. Использование фабрики для создания фигур по строковому идентификатору.
"""

import math
# Импортируем все необходимые компоненты из библиотеки
from src.shape_calculator import (
    Circle,
    Triangle,
    Shape,
    create_shape,
    InvalidDimensionsError,
    InvalidTriangleError,
)


def demonstrate_basic_usage():
    """Демонстрация основного функционала."""
    print("--- 1. Basic usage ---")

    # Создаем круг с радиусом 10
    try:
        circle = Circle(radius=10)
        print(f"A circle has been created: Circle(radius={circle.radius})")
        # Вычисляем и выводим площадь с форматированием до 2 знаков после запятой
        print(f"The area of the circle: {circle.area():.2f}")
        print("-" * 20)

        # Создаем египетский треугольник (прямоугольный)
        right_triangle = Triangle(a=3, b=4, c=5)
        print(f"A triangle has been created: Triangle(a={right_triangle.a}, b={right_triangle.b}, c={right_triangle.c})")
        print(f"The area of the triangle: {right_triangle.area()}")

        # Проверяем, является ли он прямоугольным
        if right_triangle.is_right_angled():
            print("This triangle is rectangular.")
        else:
            print("This triangle is not rectangular.")

    except (InvalidDimensionsError, InvalidTriangleError) as e:
        print(f"An error has occurred: {e}")

    print("\n")


def demonstrate_error_handling():
    """Демонстрация обработки исключений."""
    print("--- 2. Error handling ---")

    # Попытка создать круг с отрицательным радиусом
    try:
        print("An attempt to create a Circle(radius=-5)...")
        Circle(radius=-5)
    except InvalidDimensionsError as e:
        print(f"ERROR, as expected: {e}")
    print("-" * 20)

    # Попытка создать "невозможный" треугольник
    try:
        print("An attempt to create a Triangle(a=1, b=2, c=10)...")
        Triangle(a=1, b=2, c=10)
    except InvalidTriangleError as e:
        print(f"ERROR, as expected: {e}")

    print("\n")


def demonstrate_polymorphism():
    """Демонстрация вычисления площади без знания типа фигуры"""
    print("--- 3. Calculating the area without knowing the shape type (Polymorphism) ---")

    # Создаем список различных фигур.
    # Тип переменной 'shapes' - это list[Shape], мы работаем с общей абстракцией.
    shapes: list[Shape] = [
        Circle(1),
        Triangle(3, 4, 5),
        Triangle(10, 10, 10),
        Circle(2.5)
    ]

    print("Processing a list of different shapes in a loop:")
    for i, shape in enumerate(shapes):
        # Неизвестно Circle это или Triangle.
        # но известно, что у любого объекта 'shape' есть метод area().
        shape_type = type(shape).__name__
        area = shape.area()
        print(f"  Shape #{i + 1} (type: {shape_type}): area = {area:.2f}")

    print("\n")


def demonstrate_factory():
    """Демонстрация использования фабрики для создания фигур"""
    print("--- 4. Using the factory to create shapes ---")
    # Если данные для фигур приходят извне, например, из JSON или БД
    shape_data = [
        {"type": "circle", "params": {"radius": 7}},
        {"type": "triangle", "params": {"a": 5, "b": 12, "c": 13}},
        {"type": "CiRCle", "params": {"radius": 1}},  # Проверка на нечувствительность к регистру
    ]

    created_shapes = []
    for data in shape_data:
        try:
            # Используем фабричную функцию create_shape
            shape = create_shape(data["type"], **data["params"])
            created_shapes.append(shape)
            print(f"The factory has successfully created a figure: {type(shape).__name__} with parameters {data['params']}")
        except (ValueError, InvalidDimensionsError, InvalidTriangleError) as e:
            print(f"Error when creating a shape through the factory: {e}")

    print("-" * 20)
    print("Squares of shapes created through the factory: ")
    for shape in created_shapes:
        print(f" - Area {type(shape).__name__}: {shape.area():.2f}")

    print("\n")


if __name__ == "__main__":
    print("=" * 40)
    print("Demonstration of the shape_calculator library")
    print("=" * 40 + "\n")

    demonstrate_basic_usage()
    demonstrate_error_handling()
    demonstrate_polymorphism()
    demonstrate_factory()