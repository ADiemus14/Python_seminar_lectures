# Задача 12: 
# Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.


import math
s =int(input('Введите число, которое является суммой 2 натуральных чисел от 1 до  1000:'))
p =int(input('Введите число, которое является произведением 2 натуральных чисел от 1 до  1000:'))
d=s*s-4*1*p
print(d)

if d > 0:
    x = (s + math.sqrt(d)) // (2 * 1)
    y = (s - math.sqrt(d)) // (2 * 1)
    print('Загаданные Петей числа', x, 'и', y )
elif d == 0:
    x = s // (2 * 1)
    print('x,y = ', x)
else:
    print("Введите натуральные числа в заданном диапазоне")

# Y=5-X 
# P = X * (5-X) = 6
# X*5 - X^2 - 6 = 0 


# X^2 -5*X + 6 = 0 
#d=s*s-4*1*p
#x=-5+-