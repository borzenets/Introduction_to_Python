# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

user_input_a1,\
    user_input_n,\
    user_input_d = (int(item) for item in input('Введите через пробел а1, n, и d: ').strip().split())


def my_progressiya(a1, n, d):
    new_progressiya = []
    for i in range(n):
        new_progressiya.append(a1 + (n-i) * d)
    return new_progressiya


print(my_progressiya(user_input_a1, user_input_n, user_input_d))
