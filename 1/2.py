# В некоторой школе решили набрать три новых математических класса и оборудовать
# кабинеты для них новыми партами. За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт,
# которое нужно приобрести для них.
# **Input:**
# 20
# 21
# 22
# **Output:**
# 32

class_one = 20
class_two = 21
class_three = 22

count_desk_class_one = (class_one + 1) // 2
count_desk_class_two = (class_two + 1) // 2
count_desk_class_3 = (class_three + 1) // 2

print(f' Для 3 классов нужно приобрести {count_desk_class_one + count_desk_class_two + count_desk_class_3} парт')

