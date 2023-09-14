# Задача 36: 
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число 
# строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1  2 3 4 5 6

# 2  4 6 8 10 12
# 3  6 9 12 15 18
# 4  8 12 16 20 24
# 5  10 15 20 25 30
# 6  12 18 24 30 36

def print_operation_table(operation, num_rows, num_columns):
    for i in range(1,num_rows+1):
        result = []
        for j in range(1,num_columns+1):
           num =  operation(i,j)
           result.append(str(num).ljust(3))
           if len(result) == num_rows:
            for i in result:
                print(i, end = " ")
            print()
    

rows = int(input('Введите число столбцов: '))
columns = int(input('Введите число строк: '))
# mult_tab= print_operation_table(lambda x,y: x*y, rows, columns)
# print(mult_tab)


print_operation_table(lambda x,y: x*y, rows, columns)

# # __________________________решение 2

# row = int(input('Введите число столбцов: '))
# columns = int(input('Введите число строк: '))

# def print_operation_table(operation, row, col):
#     for row in range(1, row+1):
#         for col in range(1,col+1):
#             print("{: >3}".format(operation(row, col)), end="")
#         print()

# print_operation_table(lambda row, columns: row * columns, row, columns)