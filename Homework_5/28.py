# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

num_1 = 3
num_2 = 7


def my_sum(num_one, num_two):
    if num_two == 0:
        return num_one
    else:
        return my_sum(num_one, num_two - 1) + 1


print(my_sum(num_1, num_2))
