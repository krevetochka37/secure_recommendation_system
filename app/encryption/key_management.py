import os
import logging
from cryptography.fernet import Fernet

# Настройка логирования
logger = logging.getLogger(__name__)

def generate_and_save_key(key_path):
    """
    Генерирует новый ключ шифрования и сохраняет его в указанный файл.

    Аргументы:
        key_path (str): Путь к файлу для сохранения ключа.
    """
    try:
        key = Fernet.generate_key()
        with open(key_path, 'wb') as key_file:
            key_file.write(key)
        logger.info(f"New encryption key generated and saved to {key_path}.")
    except Exception as e:
        logger.error(f"Error generating or saving encryption key: {e}")
        raise

def load_key(key_path):
    """
    Загружает ключ шифрования из указанного файла.

    Аргументы:
        key_path (str): Путь к файлу, содержащему ключ.

    Возвращает:
        bytes: Загруженный ключ шифрования.
    """
    try:
        with open(key_path, 'rb') as key_file:
            key = key_file.read()
        logger.info(f"Encryption key loaded from {key_path}.")
        return key
    except Exception as e:
        logger.error(f"Error loading encryption key: {e}")
        raise

def update_key(key_path):
    """
    Обновляет ключ шифрования, генерируя новый и сохраняя его в указанный файл.

    Аргументы:
        key_path (str): Путь к файлу для сохранения нового ключа.
    """
    try:
        generate_and_save_key(key_path)
        logger.info(f"Encryption key updated and saved to {key_path}.")
    except Exception as e:
        logger.error(f"Error updating encryption key: {e}")
        raise

# Пример использования
if __name__ == "__main__":
    key_path = "secret.key"
    generate_and_save_key(key_path)
    key = load_key(key_path)
    print(f"Loaded key: {key}")
