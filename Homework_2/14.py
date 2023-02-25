# Задача 14:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

def get_number_in_console(message: str):
    flag = True
    user_insert = str()
    while flag:
        user_insert = input(message)
        if user_insert.isdigit():
            user_insert = int(user_insert)
            flag = False
        else:
            print('Вы ввели не число')
    return user_insert


user_digit = get_number_in_console('Введите число до которого вы хотите получить числа степени двойки: ')

count = 1
result = ''
while 2 ** count <= user_digit:
    result += f'{2 ** count}, '
    count += 1

print(result)
