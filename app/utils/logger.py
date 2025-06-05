import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(log_file='app.log', level=logging.INFO):
    """
    Настраивает и возвращает логгер с заданным уровнем логирования и файлом для записи логов.

    Аргументы:
        log_file (str): Имя файла для записи логов.
        level: Уровень логирования (по умолчанию INFO).

    Возвращает:
        logging.Logger: Настроенный логгер.
    """
    # Создаем директорию для логов, если она не существует
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_path = os.path.join(log_dir, log_file)

    # Создаем логгер
    logger = logging.getLogger(__name__)
    logger.setLevel(level)

    # Создаем обработчик для записи логов в файл с ротацией
    handler = RotatingFileHandler(log_path, maxBytes=5*1024*1024, backupCount=2)
    handler.setLevel(level)

    # Создаем форматтер и добавляем его к обработчику
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(handler)

    return logger

# Пример использования
if __name__ == "__main__":
    logger = setup_logger()
    logger.info("This is an info message.")
