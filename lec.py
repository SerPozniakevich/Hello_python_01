from multiprocessing.sharedctypes import Value
from random import shuffle
from typing import Iterable
from unittest.mock import patch


# print ('Hello World')
# value = None #None - назначение пустой переменной.
# # # name = Sergei
# # print(type(value))
# a = 123
# b = 1.23
# # print(type(a))
# # print(type(b))
# value = 12334
# # print(type(value))
# s = 'hello world'

# # print(type(s)) #вывод строки

# print(a, '-',b, '-',s)
# print('{1} - {2} - {0}'.format(a, b, s)) #форматированный вывод с указанием порядка вывода
# print(f'{a} - {b} - {s}') #форматированный вывод


# f = True
# print(f)

# list = [1, 2, 3]
# print(list)

# print - выводит данные
# input - принимает данные

# print('Введите a')
# a = int(input()) # указание вида данных для идентификации программой
# print('Введите b')
# b = int(input())

# print(a,' + ', b, ' = ', a+b)
# print('{} {}'.format(a, b)) #форматированный вывод с указанием порядка вывода
# print(f'{a} {b}') #форматированный вывод  

# Арифметические операции
# +, -, *, /, %, //, **
# // - деление в целых числах (без остатка)
# % - вывод остатка от деления
# ** - возведение в степень
#c = round(a * b, 5) - округление до пяти знаков после запятой
# a = 1.312312
# b = 3
# c = round(a * b, 5)
# print(c)

# (), Сщкращённые опреции присваивания

# a = 3
# a += 5
# print(a)

# Логические операции
# <, >, <=, >=, ==, !=
# not, and, or - не путать с &, |, ^,
# is, is not, in, not in

# func = 1
# T = 4
# x = 2

# print(func<T>x)

f = [1,2,3,4]

# print(f)
# print(2 in f) # проверка наличия значения в списке
# print(not 2 in f)


# is_odd = f[0] % 2 == 0 #проверка на чётность конкретного числа var1
# is_odd = not f[0] % 2 #проверка на чётность конкретного числа var2
# print(is_odd)

# Управляющие конструкции: if; if-else
# print('Введите a')
# a = int(input('a = ')) # упрощённый способ ввода/принятия данных (без print('Введите а'))
# # print('Введите b')
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)


# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print("Ильнар - топ")
# else:
#     print('Привет, ', username)

# WHILE

# original = 23456789
# inverted = 0
# while original != 0: # while используется как с else , так и без него
#     inverted = inverted * 10 + (original % 10) # переворот числа
#     original //= 10
# else:
#     print('Пожалуй ')
#     print('хватит ')
# print(inverted)

# FOR
# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)

# list = range(10)# вывод значений от нуля до 9
# for i in list:
#     print(i)

# list = range(1, 10)# вывод значений от 1 до 9
# for i in list:
#     print(i)


# list = range(1, 10, 2)# вывод значений от 1 до 9, третий аргумент - приращение (увеличение на 2)
# for i in list:
#     print(i)


# СТРОКИ

# text = 'съешь ещё этих мягких французских булок'

# help(text.istitle) # help - подсказка команд (команда заносится в скобочки), затем "запуск"
# print(len(text)) # подсчёт знаков в тексте
# print('ещё' in text) # поиск слова в тексте
# print(text.isdigit()) # проверка заначений на принадлежность к числам
# print(text.islower()) # проверка символов на нижний регистр
# print(text.replace('ещё','больше')) # замена слова на слово
# print(text[0])        # показывает первый символ строки/массива
# print(text[len(text)-1]) # последний символ строки/массива
# print(text[-1])          # последний символ строки/массива
# print(text[:])          # весь текст
# print(text[0:5])        # текст в выбранном промежутке

#ФУНКЦИИ

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 2.3
# print(f(arg))
# print(type(f(arg)))

# Lection 002
# ___________________________________

# РАБОТА С ФАЙЛАМИ
# a - открытие для добавления данных
# r - открытие для чтения данных
# w - открытие для записи данных

# colors = ['red', 'green', 'blue'] #Набор данных, в качестве набора данных выступает список
# data = open('file.txt', 'w') # Создаём переменную "data", связываем её с файлом(путь к файлу), указывая мод как будем работать (а)
# data.writelines(colors) # разделителей не будет
# data.close()

# colors = ['red', 'green', 'blue'] #Набор данных, в качестве набора данных выступает список
# data = open('file.txt', 'w') # Создаём переменную "data", связываем её с файлом(путь к файлу), указывая мод как будем работать (а)
# data.writelines(colors) # разделителей не будет
# data.write('\nLINE 2\n')  # дописывание данных в файл с новой строки и заканчивая новой строкой
# data.write('LINE 3\n')
# data.close() # закрытие связи с файлом - обязательно!

# конструкция with для работы с файлами
# в данной конструкции не требуется закрытие файла, закрытие происходит автоматически,
# после завершения кода

# with open('file.txt', 'w') as data: # "as data" - создание переменной
#     data.write('line 1\n')
#     data.write('line 2\n') 


# patch = 'file.txt' # создание пути к файлу
# data = open(patch, 'r') # открытие в режиме чтения
# for line in data:  # цикл для чтения данных из файла
#     print(line)
# data.close() # разрыв связи с файлом

# exit()                  # позволяет не выполнять код после него (вместо комментирования)

# ОТКРЫТИЕ КОДА ИЗ ФАЙЛА

# import hello

# print(hello.f(1))

# ПРИМЕНЕНИЕ ПСЕВДОНИМА

# import hello as h

# print(h.f(1))

# ОПЯТЬ ФУНКЦИИ

# def new_string (symbol, count = 3):
#     return symbol * count

# print(new_string('!', 5)) # result: !!!!!
# print(new_string('!'))    # result: !!!
# print(new_string(4))      # result: 12

# ФУНКЦИЯ ПЕРЕДАЧИ НЕОГРАНИЧЕННОГО ЧИСЛА АРГУМЕНТОВю
# СТРОКИ (str)

# def concatenatio(*params): # * означает неограниченное кол-во аргументов
#     res: str = ""
#     for item in params:
#         res += item
#     return res


# print(concatenatio('a', 's', 'd', 'w')) # result asdw
# print(concatenatio('a', '1', 'd', '2')) # result a1d2
# print(concatenatio(1, 2, 3, 4)) # result TypeError  c "str" так нельзя)

# ЧИСЛА (int)

# def concatenatio(*params): # * означает неограниченное кол-во аргументов
#     res: int = 0
#     for item in params:
#         res += item
#     return res

# print(concatenatio(1, 2, 3, 4)) # result 10

# ФУНКЦИЯ РЯДА ФИБОНАЧЧИ

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# # ВЫВОД НА ПЕЧАТЬ 

# list = []
# for e in range (1, 10): # вывод рядя Фибоначчи для чисел от 1 до 10
#     list.append(fib(e))
# print(list)  # result: [1, 1, 2, 3, 5, 8, 13, 21, 34]

# LECTION 3 LAMBDA
#--------------------------------------------------------------

# def f (x):         # присваивание переменной функцию 
#     return x**2

# g = f

# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))

# Функция функций с одной переменной

# def calc1(x):
#     return x + 10

# def calc2(x):
#     return x * 10

# def math(op, x):
#     print(op(x))

# Функция функций с двумя переменными

# def sum(x, y):
#     return x + y

# sum = lambda x, y: x + y # Упрощённая версия записи функции (Лямбда)


# def mult(x, y):
#     return x * y

# def calc(op, a, b):
#     print(op(a, b))   

# calc(lambda x, y: x + y, 4, 5) # Лямбду можно прописать в вызов функции

# calc(sum, 4, 5) # вызываем конкретную функцию

# List Comprehension  - упрощённое создание списков
# 1. [exp for item in iterable] - exp - название, iterable - условие
# 2. [exp for item in iterable (if conditional)]
# [exp <if condetional> for item in iterable (if conditional)] - не использовать)))

# list = []  # обычное создание листа

# for i  in range(1, 100):
#     list.append(i)
# print(list)

list = [i for i in range(1, 21)] # создание списка без условий
print(list)

list = [i for i in range(1, 21) if i % 2 == 0] # создание списка с условиями
print(list)

list = [(i, i) for i in range(1, 21) if i % 2 == 0] # создание списка кортежей с условиями
print(list)

# создание списка кортежей (число и его куб) с условиями и функцией

def f(x):
    return x ** 3

list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
print(list)