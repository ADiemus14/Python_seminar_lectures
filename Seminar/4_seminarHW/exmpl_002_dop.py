# Задача 2 необязательная. 
# Напишите программу, 
# которая получает целое число 
# и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.

# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
# Используйте функции

from easygui import *
a =int(enterbox('Укажите в какой системе вы хотите получить результат:\n\
2- двоичная\n\
8- восмеричная\n\
Ввод: '))
if a == 2 or a == 8: 
    num = int(enterbox('Введите число:'))
    sp = ""

    while num >= a-1:
        sp += str(num % a)
        num = num //a

    if a == 8: sp += str(num) 
    msgbox(sp[::-1])
   
     
else:
     msgbox('БЕСИШЬ')
   