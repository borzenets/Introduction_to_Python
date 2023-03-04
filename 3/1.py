# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число.

import random

len_list = int(input('Введите длину списка N: '))
shift_k = int(input('Введите сдвиг K: '))
#
#  1 вариант решения
#
# list_N_items = [i for i in range(len_list)]
# print(list_N_items)
#
# print(list_N_items[shift_k:] + list_N_items[:shift_k])
#
# #  2 вариант решения
#
# new_list = []
# count = 0
# for i in range(len_list):
#     if shift_k + i < len_list:
#         new_list.append(shift_k + i)
#     else:
#         new_list.append(count)
#         count += 1
#
# print(new_list)

#  3 вариант решения от преподавателя

my_list = [i for i in range(len_list)]
print(my_list)

for i in range(shift_k):
    my_list.insert(0, my_list.pop(-1))

print(my_list)
