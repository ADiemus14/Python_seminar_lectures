# Задача 14: 
# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.

user_number = int (input('Введите число: '))
sp = []
degree = 0
number=2
res = 0

while res < user_number:
    sp.append(res)
    res = number ** degree
    degree += 1
print(*sp)



