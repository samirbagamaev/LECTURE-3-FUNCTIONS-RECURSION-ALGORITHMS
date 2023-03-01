#ИМПОРТИРУЕМ ФАЙЛ modul1

# import modul1
# print(modul1.max1(11,15)) #ОТВЕТ: 15


#ИЛИ ЖЕ МОЖЕМ ТАК

# from modul1 import max1
# print(max1(11,15)) #ОТВЕТ: 15


#ДЛЯ ИМПОРТИРОВАНИЕ ВСЕХ ФУНКЦИЙ РАЗОМ 

# from modul1 import * #ПРОСТО ДОБАВЛЯЕМ ЗВЁЗДОЧКУ
# print(max1(11,15)) #ОТВЕТ: 15


#ТАК ЖЕ МОЖЕМ СОКРАТИТЬ НАЗВАНИЕ 

import modul1 as m1
print(m1.max1(11,15)) #ОТВЕТ: 15
