# Задача 12:
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.


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


sum_digits = get_number_in_console('Введите сумму чисел: ')
product_digits = get_number_in_console('Введите произведение чисел: ')

for i in range(sum_digits):
    for j in range(product_digits):
        if sum_digits == i + j and product_digits == i * j:
            print(f'Это числа {i} и {j}')
