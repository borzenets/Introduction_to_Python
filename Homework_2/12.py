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

#  Вариант преподавателя

a, b, c = -1, sum_digits, -product_digits
def roots(a, b, c):
    discr = b**2 - 4*a*c
    if discr > 0:
        x1 = (-b - discr ** 0.5) / 2 * a
        x2 = (-b + discr ** 0.5) / 2 * a
        return int(x1), int(x2)
    elif discr == 0:
        x = -b / 2 * a
        return int(x)
    else:
        return 'Петя обманул Катю'

print(roots(a, b, c))