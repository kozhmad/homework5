import math
import random
from typing import List
import argparse

# Создание парсера аргументов командной строки
parser = argparse.ArgumentParser(description="Генерация простых чисел и их перемешивание")
parser.add_argument('prime_count', type=int, help='Количество простых чисел для генерации')
parser.add_argument('seed_count', type=int, help='Начальное значение для генератора случайных чисел')

# Чтение аргументов командной строки
args = parser.parse_args()
prime_count = args.prime_count
seed_count = args.seed_count


def is_prime(x: int) -> bool:
    """
    Функция для проверки, является ли число простым

    :param x: целое число
    :return: True/False
    """
    
    isprime = True
    for y in range(2, int(math.sqrt(x) + 1)):
            if x % y == 0: 
                isprime = False
                break
    return isprime



def primes(count: int, seed_count: int) -> List[int]:
    """
    Функция для генерации списка простых чисел

    :param count: целое число, обозначающее необходимое кол-во простых чисел
    :return: список простых чисел
    """
    x = 2
    prime_numbers=[]
    while len(prime_numbers) < count:
        if is_prime(x):
            prime_numbers.append(x)   
        x += 1
    random.seed(seed_count)
    random.shuffle(prime_numbers)
    return prime_numbers
    



def  checksum(x: List[int]) -> int:
    """
    Функция для расчета контрольной суммы

    :param х: список простых чисел
    :return: контрольная сумма
    """
    checksum_value = 0
    for num in x:
        checksum_value = (checksum_value + num) * 113 % 10000007
    return checksum_value

def pipeline(prime_count: int, seed_count: int) -> int:
    prime_numbers = primes(prime_count, seed_count)
    result = checksum(prime_numbers)
    # Вывод результата по одному числу в строке
    for prime in prime_numbers:
        print(prime)

pipeline(prime_count, seed_count)