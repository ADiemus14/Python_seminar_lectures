# 1 способ итерации 

sp = [55, 111, True, "sssss", [55,77,88] ]

for i in range(len(sp)):
    print(sp[i], end = " ")


# 2 способ итерации 

print(end = "\n")
for el in sp:
    print(el, end = " ")


# 3 способ итерации 

print(end = "\n")
for item in enumerate(sp):
    print(item)


    