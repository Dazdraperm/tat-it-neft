from typing import List
from math import sqrt, ceil

__all__ = (
    'get_init_primes',
    'number_is_prime',
    'NUMBER_EXCEPTION',
)

NUMBER_EXCEPTION = 'Number must be >= 1'


def get_init_primes(number: int) -> List:
    """Инициализируем список с простыми числами"""

    # В поиске простых чисел пропускаем цифру 1, поэтому добавляем ее сразу
    if number == 1:
        prime_numbers = [1, ]

    # Из-за реализации связанной с вычислением корня, добавляем 2
    else:
        prime_numbers = [1, 2]

    return prime_numbers


def number_is_prime(number: int) -> bool:
    """Выясняем простое число или нет"""

    sqrt_number = ceil(sqrt(number))

    for i in range(2, sqrt_number + 1):
        if number % i == 0:
            return False

    return True
