# Задача 1 (easy):
# fruits = {"1": 'Груша', '2': 'Киви', '3': 'Банан', '4': 'Яблоко', '5': 'Абрикос', '6': 'Апельсин'}
# for key, value in fruits.items():
#    print(key, value)

# Задача 2 (easy):

# materials = ['Доска', 'Молоток', 'Пила', 'Гвозди', 'Дрель']
# materials_buy  = ['Скотч', 'Доска', 'Изолента', 'Гвозди', 'Плитка']

# print('Материалы: {}'.format(materials))
# print('Купленные материалы: {}'.format(materials_buy))

# for mat in materials[:]:
#    for matbuy in materials_buy[:]:
#        if mat == matbuy:
#            materials.remove(matbuy)

# print('Осталось докупить: {}'.format(materials))

# Задача 3 (easy):
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# new_num = []
# print(num)

# for el in reversed(num):
#    count = num.index(el)
#   if (el % 2) == 0:
#      new_el = el/4
#     new_num.insert(0, new_el)
#    num.remove(el)

#    else:
#        el = el*2
#        num[count] = el

# print(num)
# print(new_num)

# Задача 1 (normal):

# import math

# num = [2, -5, 8, 9, -25, 25, 4]
# new_num = []

# for el in num:
#     if el > 0 and (math.sqrt(el)) % 1 == 0:
#         new_num.append(int(math.sqrt(el)))
# print(new_num)

# Задача 2 (normal):

# data = input ('Введите дату дд.мм.гггг: ')
# new_data = (data.split('.'))
# day = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое', '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое', '11': 'одинадцатое', '12': 'двенадцатое', '13': 'тренадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое'}
# mounth = {'01': 'яеваря', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'майя', '06': 'июня', '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}
# print('Сегодня {} {} {} года.'.format(day[new_data[0]],(mounth)[new_data[1]], new_data[2]))

# Задача 3 (normal):

# import random
# numbers = int(input('Введите колличество чисел: '))
# mylist = []
# n = 0
# while n < numbers:
#    mylist.append(random.randint(-100, 100))
#    n += 1
# print(mylist)

# Задача 4 (normal):

import random
number = int(input('Введите колличество чисел: '))
mylist = []
n = 0
while n < number:
    mylist.append(random.randint(0, 100))
    n += 1
print(mylist)

sort_list = set(mylist)
print(sort_list)