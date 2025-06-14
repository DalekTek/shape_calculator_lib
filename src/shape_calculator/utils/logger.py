"""Модуль для настройки централизованного логгера."""
import logging
import sys

# Создаем логгер
logger = logging.getLogger("shape_calculator")
logger.setLevel(logging.INFO)

# Создаем обработчик, который выводит логи в stdout
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)

# Создаем форматтер и добавляем его к обработчику
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
if not logger.handlers:
    logger.addHandler(handler)