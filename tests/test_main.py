import unittest
import random  
import sys
import os
# Добавляем путь к родительской директории, чтобы Python нашел main.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import is_prime, primes, checksum

class TestPrimeFunctions(unittest.TestCase):
    
    # Тест для функции проверки простоты числа
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(9))
        self.assertTrue(is_prime(29))
    
    # Тест для функции генерации списка простых чисел
    def test_primes(self):
        result = sorted(primes(10))
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(result, expected)
        self.assertEqual(len(result), 10)
    
    # Тест для функции расчета контрольной суммы
    def test_calculate_checksum(self):
        numbers = [1, 2, 6, 24]
        checksum_value = checksum(numbers)  
        expected_checksum = (((((0 + 1) * 113) % 10000007 + 2) * 113) % 10000007 + 6) * 113 % 10000007
        expected_checksum = (expected_checksum + 24) * 113 % 10000007
        self.assertEqual(checksum_value, expected_checksum)


    # Тест для расчета контрольной суммы с 1000 простыми числами
    def test_large_checksum(self):
        prime_numbers = primes(1000)
        self.assertEqual(len(prime_numbers), 1000) 
        checksum_value = checksum(prime_numbers)
        self.assertEqual(checksum_value, 7785816)  

if __name__ == "__main__":
    unittest.main()