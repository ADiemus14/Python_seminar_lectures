# # Пример ошибочного поведения в коде:

# bag_potatoes = [2, 2, 2, 1, 2, 1, 2, 2, 2, 2] # это наш мешок, в нем 2 гнилушки

# for potato in bag_potatoes: # запустим цикл перебора картошки
# 		if potato == 1:
# 				print('Замечена гнилая картошка')
# 				print('Нужно сходить выкинуть, то что нашли')
# 		else:
# 				print('Нет гнилой картошки')
# 				print('Ничего выкидывать не нужно')


# """Вот тут в блоке else и кроется ошибка, т. е. 
# мы еще не закончили перебирать мешок, а выводы уже делаем.

# Попробуем решить с флагом:"""

# bag_potatoes = [2, 2, 2, 1, 2, 1, 2, 2, 2, 2] # это наш мешок, в нем 2 гнилушки

# rot_flag = False # это наш флаг на гниль, сейчас у него значение фолз (ложь)

# for potato in bag_potatoes: # запустим цикл перебора картошки
#     if potato == 1:
#       	rot_flag = True # замечена гнилая картошка, флаг мы переводим в Тру (истина)
    
# # ниже мы смотрим на значение флага, т.е. наших наблюдений, и делаем выводы		
# if rot_flag: 
#     print('есть гнилая картошка')
#     print('Нужно сходить выкинуть, то что нашли')
# else:
#     print('нет гнилой картошки')
#     print('Ничего выкидывать не нужно')


# """А как же можно научиться пользоваться флагом?___________________________________
# например счетчик…
# Пример: посчитаем гнилую картошку:"""

# bag_potatoes = [2, 2, 2, 1, 2, 1, 2, 2, 2, 2] # это наш мешок, в нем 2 гнилушки

# count = 0 # счетчик на гниль

# for potato in bag_potatoes: # запустим цикл перебора картошки
#     if potato == 1:
#       	count += 1 # замечена гнилая картошка, увеличиваем счетчик
		
# if count > 0: # смотрим что насчитали и делаем выводы
#     print('есть гнилая картошка')
#     print('Нужно сходить выкинуть, то что нашли')
# else:
#     print('нет гнилой картошки')
#     print('Ничего выкидывать не нужно')



# """Следующий шаг на пути счетчик-флаг понимание __________________________
# того что нам не нужно считать, 
# а достаточно изменить счетчик с 0 на любое число, например 1"""

# for potato in bag_potatoes: # запустим цикл перебора картошки
#     if potato == 1:
#       	count = 1 # замечена гнилая картошка, меняем счетчик
		
# if count == 1: # смотрим на счетчик и делаем выводы 
#     print('есть гнилая картошка')
#     print('Нужно сходить выкинуть, то что нашли')
# else:
#     print('нет гнилой картошки')
#     print('Ничего выкидывать не нужно')


# """Но наш счетчик уже не счетчик________________________
# у него 2 возможных значения (0, 1)
# А это прям подходит для булевых переменных, 
# которые и являются классическим флагом со значениями (True, False)"""

# count = False
# for potato in bag_potatoes: # запустим цикл перебора картошки
#     if potato == 1:
#       	count = True # замечена гнилая картошка, меняем счетчик
    
# # смотрим на "счетчик" и делаем выводы (тут можно также записать @if count:@)		
# if count == True:   
#     print('есть гнилая картошка')
#     print('Нужно сходить выкинуть, то что нашли')
# else:
#     print('нет гнилой картошки')
#     print('Ничего выкидывать не нужно')



"""Теперь если сменить имя счетчика count на rot_flag_________________
 то получится первый вариант решения, т. е. с полноценным флагом."""
 