import json
from typing import Any, Dict

def load_json(file_path: str) -> Dict[str, Any]:
    """
    Загружает данные из JSON файла.

    Аргументы:
        file_path (str): Путь к JSON файлу.

    Возвращает:
        Dict[str, Any]: Словарь с данными из JSON файла.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data: Dict[str, Any], file_path: str) -> None:
    """
    Сохраняет данные в JSON файл.

    Аргументы:
        data (Dict[str, Any]): Данные для сохранения.
        file_path (str): Путь к JSON файлу.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def validate_data(data: Dict[str, Any], required_keys: list) -> bool:
    """
    Проверяет наличие обязательных ключей в словаре данных.

    Аргументы:
        data (Dict[str, Any]): Данные для проверки.
        required_keys (list): Список обязательных ключей.

    Возвращает:
        bool: True, если все обязательные ключи присутствуют, иначе False.
    """
    return all(key in data for key in required_keys)

# Пример использования
if __name__ == "__main__":
    data = {"key1": "value1", "key2": "value2"}
    file_path = "data.json"

    save_json(data, file_path)
    loaded_data = load_json(file_path)
    print(f"Loaded data: {loaded_data}")

    is_valid = validate_data(loaded_data, ["key1", "key2"])
    print(f"Data is valid: {is_valid}")
