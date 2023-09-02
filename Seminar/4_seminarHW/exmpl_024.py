# Задача 24: 
# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод 
# — на i-ом кусте выросло a[i] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, 
# находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном списке урожайности грядки.

import random

n = int(input('Введите количество кустов на грядке: '))
if n < 3:
    print("Количество кустов для ручного труда, собирайте без модуля")
    
else:
    list_urojai = random.sample(range(70), n)
    print("Количество ягод на каждом кусте:", list_urojai)
    i=0
    list_sum = []



    while i < n :
        sum =0
        
        if i == n-1:
            sum = list_urojai[i] + list_urojai[0] + list_urojai[i-1]
        else: 
            sum = list_urojai[i] + list_urojai[i+1] + list_urojai[i-1]
        
        list_sum.append(sum)
        i+=1

    print ("Сумма ягод  с трех кустов на каждом подходе", list_sum)
    print("Максимальное число ягод, которое может собрать за один заход собирающий модуль", max(list_sum))