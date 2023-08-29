# Задача 1 HARD по желанию 
# Напишите программу, которая принимает на вход целое или дробное число 
# и выдаёт количество цифр в числе.
# 456 -> 3
# 0 -> 1
# 89,126 -> 5
# 0,001->4

from decimal import Decimal

n = Decimal(input('Введите число: '))

if n < 0:
    n =abs(n)
    print("положительное ", n)

left = int(n)
right = n - left
print( "левое и правое", left, right)
count = 0
    
if int(n) == 0:
    count = 1
    print("т.к. 0 то",count)



while left > 0:
    count += 1
    left = left // 10


while right % 1 != 0:
    count += 1
    right *=10

print( count)

# while n != int(n):
#     n *=10
    

# while n > 0:
#     count += 1
#     n = n%10


# left = int(n)
# right = Decimal(n - left)

# count = 0
# print(right)



# print(left, right)
# print("Количество цифр в числе:", count)
