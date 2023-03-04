import random

my_list = [random.randint(0, 10) for i in range(10)]
print(my_list)

#  Вариант решения 1

# my_dict = {}
# for i in my_list:
#     my_dict[i] = my_dict.get(i, 0) + 1
#
# print(my_dict)
#
# new_list = []
#
# for key, value in my_dict.items():
#     if value == 1:
#         new_list.append(key)
#
# print(new_list)

#  Вариант решения 2

new_list = []

for item in my_list:
    if my_list.count(item) == 1:
        new_list.append(item)

print(new_list)