import pandas as pd
import logging
from typing import List, Dict, Any

# Настройка логирования
logger = logging.getLogger(__name__)

def load_data(data_source: str) -> List[Dict[str, Any]]:
    """
    Загружает данные из указанного источника.

    Аргументы:
        data_source (str): Путь к источнику данных (например, файл CSV).

    Возвращает:
        List[Dict[str, Any]]: Список словарей, представляющих строки данных.
    """
    try:
        # Пример загрузки данных из CSV файла
        data = pd.read_csv(data_source)
        logger.info(f"Data loaded successfully from {data_source}.")
        return data.to_dict('records')
    except Exception as e:
        logger.error(f"Error loading data from {data_source}: {e}")
        raise

def clean_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Очищает данные, удаляя или исправляя некорректные записи.

    Аргументы:
        data (List[Dict[str, Any]]): Исходные данные.

    Возвращает:
        List[Dict[str, Any]]: Очищенные данные.
    """
    try:
        # Пример: удаление записей с отсутствующими значениями
        cleaned_data = [record for record in data if all(value is not None for value in record.values())]
        logger.info("Data cleaned successfully.")
        return cleaned_data
    except Exception as e:
        logger.error(f"Error cleaning data: {e}")
        raise

def normalize_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Нормализует данные, приводя их к единому формату.

    Аргументы:
        data (List[Dict[str, Any]]): Исходные данные.

    Возвращает:
        List[Dict[str, Any]]: Нормализованные данные.
    """
    try:
        # Пример: приведение строковых значений к нижнему регистру
        normalized_data = [{k: v.lower() if isinstance(v, str) else v for k, v in record.items()} for record in data]
        logger.info("Data normalized successfully.")
        return normalized_data
    except Exception as e:
        logger.error(f"Error normalizing data: {e}")
        raise

def preprocess_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Предварительно обрабатывает данные, применяя очистку и нормализацию.

    Аргументы:
        data (List[Dict[str, Any]]): Исходные данные.

    Возвращает:
        List[Dict[str, Any]]: Предварительно обработанные данные.
    """
    try:
        cleaned_data = clean_data(data)
        normalized_data = normalize_data(cleaned_data)
        logger.info("Data preprocessing completed successfully.")
        return normalized_data
    except Exception as e:
        logger.error(f"Error preprocessing data: {e}")
        raise

# Пример использования
if __name__ == "__main__":
    data_source = "data.csv"
    data = load_data(data_source)
    processed_data = preprocess_data(data)
    print(f"Processed data: {processed_data}")
