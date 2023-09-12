# Задача НЕГАФИБОНАЧЧИ по желанию
# Задайте число.
# Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def Fibonacci (m):
    fib1 = fib2 = 1
    sp=[fib1, fib2]
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        sp.append(fib2)
    return sp

def negative_Fibonacci(sp):
    sp1 = [0, ]
    for i, v in enumerate(sp): 
        if i%2 != 0:
            v = -v
        sp1.append(v)
    return sp1



n = int(input("Номер элемента ряда Фибоначчи: "))
sp_Fib = Fibonacci(n)   
# print(sp_Fib)
neg_Fib = negative_Fibonacci(sp_Fib)
# print(neg_Fib)
sp2 = list(reversed(neg_Fib))
# print(sp2)

list_fibonacci = sp2 +  sp_Fib
print(f"Негафибоначи для числа {n}:\n{list_fibonacci}")


 




