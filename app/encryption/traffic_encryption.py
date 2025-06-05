from cryptography.fernet import Fernet
from .key_management import load_key
import logging

# Настройка логирования
logger = logging.getLogger(__name__)

def generate_key():
    """
    Генерирует новый ключ шифрования.

    Возвращает:
        bytes: Сгенерированный ключ.
    """
    return Fernet.generate_key()

def encrypt_data(data, key):
    """
    Шифрует данные с использованием предоставленного ключа.

    Аргументы:
        data (bytes): Данные для шифрования.
        key (bytes): Ключ шифрования.

    Возвращает:
        bytes: Зашифрованные данные.
    """
    try:
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)
        logger.info("Data encrypted successfully.")
        return encrypted_data
    except Exception as e:
        logger.error(f"Error during encryption: {e}")
        raise

def decrypt_data(encrypted_data, key):
    """
    Дешифрует данные с использованием предоставленного ключа.

    Аргументы:
        encrypted_data (bytes): Зашифрованные данные.
        key (bytes): Ключ шифрования.

    Возвращает:
        bytes: Дешифрованные данные.
    """
    try:
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)
        logger.info("Data decrypted successfully.")
        return decrypted_data
    except Exception as e:
        logger.error(f"Error during decryption: {e}")
        raise

def setup_encryption(config):
    """
    Настраивает шифрование с использованием предоставленной конфигурации.

    Аргументы:
        config (dict): Конфигурация приложения.
    """
    try:
        key = load_key(config["encryption_key"])
        # Здесь можно добавить дополнительную логику настройки шифрования
        logger.info("Encryption setup completed with the provided key.")
    except Exception as e:
        logger.error(f"Error during encryption setup: {e}")
        raise
