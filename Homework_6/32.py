# Задача 32:
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума
# и не больше заданного максимума)
import random
from typing import Any, List

quantity_items_list = 6

first_number,\
    last_number = (int(i) for i in input('Введите через пробел мин. и макс. значения диапазона: ').strip().split())


def get_random_number_list(quantity_items: int, max_item=100, min_item=0) -> list:
    return [random.randint(min_item, max_item) for _ in range(quantity_items)]


def get_range_indexes(input_list: list, min_item: int, max_item: int) -> list:
    return [i[0] for i in enumerate(input_list) if min_item <= i[1] <= max_item]


random_list = get_random_number_list(quantity_items_list)
print(random_list)
print(get_range_indexes(random_list, first_number, last_number))
