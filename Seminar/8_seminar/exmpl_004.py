# Дан список чисел. 
# Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу 
# образуют одну пару,
# которую необходимо посчитать.
# Вводится список чисел. 
# Все числа списка находятся на разных строках.

a = input().split()
print(sum(a.count(x) - 1 for x in a) // 2)