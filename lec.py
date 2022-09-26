from multiprocessing.sharedctypes import Value


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

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2.3
print(f(arg))
print(type(f(arg)))