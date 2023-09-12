# Задача НЕГАФИБОНАЧЧИ по желанию
# Задайте число.
# Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


fib1 = fib2 = 1
 
n = int(input("Номер элемента ряда Фибоначчи: "))
sp=[fib1, fib2]

 
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    sp.append(fib2)
print(sp)

sp1 = [0, ]
for i, v in enumerate(sp): 
    if i%2 != 0:
        v = -v
    sp1.append(v)

print(sp1)    


sp2 = list(reversed(sp1))
print(sp2)

list_fibonacci = sp2 +  sp
print(list_fibonacci)









# sp2 = list(reversed(sp))

# # i=1
# # for i, el in sp2:
# #     el = el *-1
# #     i+=2
    
# print(sp2)

# print(type(sp2[1]))
