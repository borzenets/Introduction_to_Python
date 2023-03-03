# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random

random_max = 100
random_min = 0
temp_dict = dict()
temp_index = 0


len_list = int(input('Введите длину генерируемого списка: '))

random_list = [random.randint(random_min, random_max) for _ in range(len_list)]
print(random_list)

search_number = int(input('Введите число для поиска: '))

for i in range(len(random_list)):
    temp_dict[random_list[i]] = temp_dict.get(random_list[i], 0) + 1
    if abs(random_list[temp_index] - search_number) > abs(random_list[i] - search_number):
        temp_index = i

if temp_dict.get(search_number):
    print(f'Число {search_number} - {temp_dict[search_number]} раз встречается в множестве')
else:
    print(f'Нет такого элемента, самый близкий по значению {random_list[temp_index]}'
          + f' встречается {temp_dict.get(random_list[temp_index])} - раз.')

print(temp_dict)
