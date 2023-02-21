# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

user_input_number = int(input('Введите целое неотрицательное число, факториал которого хотите получить: '))

if user_input_number == 0:
    print('1')
else:
    count = 1
    factorial = 1
    while count < user_input_number:
        factorial = factorial * (count + 1)
        count += 1

    print(factorial)
