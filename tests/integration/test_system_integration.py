import unittest
from app.main import main
from app.config import load_config
from unittest.mock import patch

class TestSystemIntegration(unittest.TestCase):
    @patch('app.main.setup_encryption')
    @patch('app.recommendation.recommendation_engine.RecommendationEngine.run')
    def test_system_integration(self, mock_run, mock_setup_encryption):
        """Тестирование интеграции системы."""
        # Настройка моков
        mock_setup_encryption.return_value = None
        mock_run.return_value = None

        # Загрузка конфигурации
        config = load_config()

        # Запуск основной функции
        main()

        # Проверка, что функции были вызваны
        mock_setup_encryption.assert_called_once_with(config)
        mock_run.assert_called_once()

if __name__ == "__main__":
    unittest.main()
