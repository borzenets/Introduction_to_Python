# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

three_digit_number = int(input('Введите трехзначное число: '))
result = (three_digit_number % 10) + (three_digit_number // 10 % 10) + (three_digit_number // 100)
print(f'Сумма чисел трехзначного числа равна: {result}')