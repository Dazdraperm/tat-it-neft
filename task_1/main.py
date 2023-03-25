"""Первое задание. Все простые числа до N"""

from utils import get_init_primes, number_is_prime, NUMBER_EXCEPTION
from typing import List


def get_prime_numbers(target_n: int) -> List:
    """Получение списка простых чисел до target_n(n)

    :param target_n: Число до которого ищем все простые числа

    :return prime_numbers: Возвращаем список всех простых чисел
    """
    if target_n <= 0:
        raise TypeError(NUMBER_EXCEPTION)

    prime_numbers = get_init_primes(number=target_n)

    # Прибавляем 1, если нужны числа до n включительно
    last_n = target_n + 1

    for number in range(2, last_n):
        if number_is_prime(number=number):
            prime_numbers.append(number)

    return prime_numbers


def main():
    target_n = int(input())
    prime_numbers = get_prime_numbers(target_n)
    print(prime_numbers)


main()
