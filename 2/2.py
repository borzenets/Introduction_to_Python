# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.


number = int(input('Введите число: '))

fibo_1 = 0
fibo_2 = 1
fibo_result = 0
index = 3

while fibo_result < number:
    fibo_result = fibo_1 + fibo_2
    fibo_1 = fibo_2
    fibo_2 = fibo_result
    if fibo_result == number:
        print(index)
    elif fibo_result > number:
        print('-1')
    index += 1