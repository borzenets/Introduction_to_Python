# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no


col_chocolate = int(input('Сколько долек в длину: '))
row_chocolate = int(input('Сколько долек в ширину: '))
cell_quantity = int(input('Сколько долек вы хотите отломить одним действием: '))
if (cell_quantity % col_chocolate == 0 and cell_quantity / col_chocolate < row_chocolate or
    cell_quantity % row_chocolate == 0 and cell_quantity / row_chocolate < col_chocolate):

    print('Вы можете это сделать, приятного аппетита!')
else:
    print('Вы это сделать не сможете.')
