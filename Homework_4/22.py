# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

quantity_items_in_set_one = int(input('Введите кол-во элементов первого множества: '))
quantity_items_in_set_two = int(input('Введите кол-во элементов второго множества: '))


def set_console_input(quantity, message):
    print(message)
    user_set = set()
    for i in range(quantity):
        user_set.add(input(f'Введите {i + 1} элемент множества: '))
    return user_set


user_set_one = set_console_input(quantity_items_in_set_one, 'Введите элементы первого множества: ')
user_set_two = set_console_input(quantity_items_in_set_two, 'Введите элементы второго множества: ')

print(sorted(user_set_one.intersection(user_set_two)))
