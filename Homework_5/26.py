# Задача 26: Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

number = 3
power = 5


def my_pow(number, power):
    if power > 1:
        return my_pow(number, power - 1) * number
    else:
        return number


print(f'Число {number} в степени {power} это {my_pow(number, power)}')
