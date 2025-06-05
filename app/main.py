from config import load_config
from encryption.traffic_encryption import setup_encryption
from recommendation.recommendation_engine import RecommendationEngine
from utils.logger import setup_logger

# Настройка логирования
logger = setup_logger()

def main():
    try:
        # Загрузка конфигурации
        config = load_config()
        logger.info("Configuration loaded successfully.")

        # Настройка шифрования
        setup_encryption(config)
        logger.info("Encryption setup completed.")

        # Инициализация и запуск рекомендательной системы
        engine = RecommendationEngine(config)
        engine.run()
        logger.info("Recommendation engine started successfully.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
