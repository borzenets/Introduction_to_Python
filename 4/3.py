# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]
import random

list_numbers = [random.randint(1000, 9999) for _ in range(7)]
print(list_numbers)

search_number = int(input('Введите цифру: '))
for i in range(len(list_numbers)):
    list_numbers[i] = int(str(list_numbers[i]).replace(str(search_number), ''))
print(list_numbers)

for i in range(len(list_numbers)):
    while list_numbers[i] > 9:
        list_numbers[i] = sum([int(digit) for digit in str(list_numbers[i])])
print(list_numbers)

print(set(list_numbers))
