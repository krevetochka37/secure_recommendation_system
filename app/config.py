import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

def load_config():
    """
    Загружает конфигурацию приложения из переменных окружения.

    Возвращает:
        dict: Словарь с параметрами конфигурации.
    """
    config = {
        "encryption_key": os.getenv("ENCRYPTION_KEY"),
        "database_url": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
        "debug_mode": os.getenv("DEBUG_MODE", "False") == "True",
        # Добавьте другие параметры конфигурации по мере необходимости
    }

    # Проверка обязательных параметров
    if not all([config["encryption_key"], config["database_url"]]):
        raise ValueError("Отсутствуют обязательные параметры конфигурации.")

    return config

# Пример использования
if __name__ == "__main__":
    config = load_config()
    print("Конфигурация загружена:", config)
