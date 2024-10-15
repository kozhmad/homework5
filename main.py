import math
import random
from typing import List


seed_count=100
prime_count=1000

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



def primes(count: int) -> List[int]:
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

def pipeline() -> int:
    prime_numbers = primes(prime_count)
    result = checksum(prime_numbers)
    return result



if __name__ == "__main__":
    result = pipeline()
    print(result)