# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.


import random

my_list = [random.randint(1, 10) for _ in range(10)]
count_dict = {}

print(my_list)

#   Мое решение

for i in my_list:
    if count_dict.get(i, 0):
        print(f'{str(i)}_{count_dict.get(i)}', end=', ')
    else:
        print(i, end=', ')

    count_dict[i] = count_dict.get(i, 0) + 1

#  Решение преподавателя

# for i in my_list:
#     count_dict[i] = count_dict.get(i, 0) + 1
#     print(i if count_dict.get(i) == 1 else f'{i}_{count_dict.get(i) - 1}', end=', ')
