# Задача 10:
# На столе лежат, n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random


count_heads = 0
count_tails = 0
quantity_coins = None
coins = ''

check_status = True
while check_status:
    quantity_coins = int(input('Введите количество монет: '))
    if quantity_coins > 0:
        check_status = False
    else:
        print('Введите положительное число.')

if quantity_coins == 1:
    print('\nМонета всего одна, переворачивать нечего.')
else:
    for i in range(quantity_coins):
        temp = random.randint(0, 1)
        if temp == 0:
            count_heads += 1
            coins += 'Ⓗ '
        else:
            count_tails += 1
            coins += '⑤ '

    print(f'\n{coins}\nⒽ - {count_heads}, ⑤ - {count_tails}\n')
    print(f'Перевернуть нужно {count_heads} монет с орлом Ⓗ' if count_heads < count_tails
          else f'Перевернуть нужно {count_tails} монет с решкой ⑤')
