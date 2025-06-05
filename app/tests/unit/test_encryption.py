import unittest
from app.encryption.traffic_encryption import encrypt_data, decrypt_data
from app.encryption.key_management import generate_and_save_key, load_key

class TestEncryption(unittest.TestCase):
    def setUp(self):
        """Настройка тестовой среды."""
        self.test_key_path = "test_key.key"
        self.test_data = b"Test data for encryption"
        generate_and_save_key(self.test_key_path)
        self.key = load_key(self.test_key_path)

    def tearDown(self):
        """Очистка после выполнения тестов."""
        import os
        if os.path.exists(self.test_key_path):
            os.remove(self.test_key_path)

    def test_encrypt_decrypt(self):
        """Тестирование шифрования и дешифрования данных."""
        encrypted_data = encrypt_data(self.test_data, self.key)
        self.assertNotEqual(self.test_data, encrypted_data, "Data should be encrypted.")

        decrypted_data = decrypt_data(encrypted_data, self.key)
        self.assertEqual(self.test_data, decrypted_data, "Decrypted data should match original data.")

    def test_encrypt_decrypt_with_wrong_key(self):
        """Тестирование шифрования и дешифрования с неправильным ключом."""
        encrypted_data = encrypt_data(self.test_data, self.key)
        wrong_key = b"wrong_key_12345678901234567890123456789012="  # Неправильный ключ

        with self.assertRaises(Exception):
            decrypt_data(encrypted_data, wrong_key)

if __name__ == "__main__":
    unittest.main()
