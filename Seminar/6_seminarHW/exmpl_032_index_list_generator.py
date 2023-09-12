# Задача 32: 
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). 
# Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# от 33 до  200
# Ответ: [2, 3]

from random import randint

num1 = int(input('Ввведите первое число диапазона: '))
num2 = int(input('Ввведите второе число диапазона: '))
size= int(input('Ввведите размер массива: '))
sp = [randint(-50, 99) for _ in range(size)]
print(sp)
def Search_index(num1, num2, sp):
    sp_result = []
    for  i, value in enumerate(sp):
        if value >=num1 and  value <= num2:
            sp_result.append(i)
    return sp_result
print(Search_index(num1, num2, sp))
