# import time

# from ast import While
# from tkinter import W


# # While = пока
# i = 1
# while i < 6:
#   print(i)
#   i += 1

# while каждый раз выполняет код внутри себя и потом проверяет свои условия и работает до тех пор пока его условия true


# Цикл for = для. Перебирает пока у него есть что перебирать в переменной
# number_list = ['1', '2', (3), [4], 5, 6, 7, 8, 9, 10]
# for number in number_list:    # для числа которое находится в number_list мы будем производить какие то действия
#     print(str(number) + 'Hola!')   # выводится 1 Hola 2 Hola ...
#     print(number)  # выводится вся последовательность чисел

# print(str(number) + 'Hola!')   # выводится 1 Hola 2 Hola ...


# print('цикл завершен')

# for number in number_list:       #мы можем выводить не все элементы
#     if number % 2 == 0:     #проверим четное ли число, если четно оно выведет код
#       print(number)
#     else:                 # если нечетно выводится hey
#       print('hey')

# # мы можем производить вычисления внутри цикла
# list_numbers_sum = 0
# for number in number_list:
#   list_numbers_sum = list_numbers_sum + number
#   print(list_numbers_sum)
# print(list_numbers_sum)


# greeting = 'Hello Python'    # Выводим каждую букву в строке
# for letter in greeting:
#   print(letter)

# greeting = 'Hello Python'    # Выводим определенную букву в строке
# for letter in greeting:
#   if letter == 'o':
#    print(letter)


# greeting = 'Hello Python'    # Выводим без определенной буквы в строке

# for letter in greeting:

#   if letter != 'P':

#     print(letter)

# Мы можем выводить строку сразу, без переменной

# for letter in 'Hello Python':
#   if letter != 'o':
#     print(letter)

# for letter in 'Hello Python':    # сколько букв в строке столько принт и выведет его раз
#    print('One more letter')

# Список в котором находятся обьекты tuple
# tuple_list = [
#   ('a', 'b'),
#   ('c', 'd'),
#   ('e', 'f')
#     ]
# print(type(tuple_list))

# for item in tuple_list:
#   print(item)

# for letter_1, letter_2 in tuple_list:
#   print(letter_1, letter_2)          #буквы выводятся отдельно a b
#                                                              c d
#                                                              e f

# for letter_1, letter_2 in tuple_list:  # буквы выводятся в столбик по очереди
#   print(letter_1)
#   print(letter_2)

#  не обязательно чтобы были только буквы, добавим цифры
# tuple_list = [
#   (
#     'a',
#     'b',
#     1
#   ),
#   (
#     'c',
#     'd',
#     4
#   ),
#   (
#     'e',
#     'f',
#     5
#   ),
#   ]                                                         #выводит =
#                                                               # a b 1
#                                                               # c d 4
#                                                               # e f 5
# for item_1_level2, item_1_level2, item_3_level2 in tuple_list:
#   print(item_1_level2, item_1_level2, item_3_level2)

# структура словарь
# dictionary = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
# for item in dictionary:
#   print(item)    #в коде мы получаем только ключи, по умолчанию когда мы обращаемся к переменной в ней хранятся только ключи, чтобы получить и ключ и значение нужно сделать вот так:
# dictionary = {
#   'key1' : 'value1',
#   'key2' : 'value2',
#   'key3' : 'value3'
#     }


# print(dictionary.items())

# x = 0


# for item in dictionary.items():   #есть метод items, который дает нам обратится и к ключу и к значению

#   x = x + 1

#   print(x)

#   print(item)

#   print('**************')


# for item in dictionary.keys():   #есть метод keys, который дает нам обратится только к ключу
#   print(item)

# for item in dictionary.values():   #есть метод values, который дает нам обратится только к значению
#   print(item)


# функция range = диапазон возвращает последовательность из чисел от 0 до параметра который мы укажем
# for x in range(5):
#   print(x)

# for x in range(11):
#   print(x)

# list_yazan = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# for item in list_yazan:
#   print(item)

# letters = 'hello'
# for item in letters:
#   print(item)


# dictionary = {

#   'yazan':45,

#   'olga':39,

#   'liuda':38
#               }
# print(dictionary.values())
# for items in dictionary.values():
# print('Дайте нам обувь  ' + str(items) + ' размера')


# print(dictionary.keys())

# for items in dictionary.keys():

#   print(items + ' живет на измаил 92')


# Цикл  WHILE = пока что. while пока у него условия true он повторяет код внутри себя  Цикл WHILE отличается от for тем что код внутри цикла выполнется до тех пор пока условие которое указано в цикле является истина.

# x = 2

# while x > 1:   # выведет бесконечно 2, потому что 2 больше 1
#   print(x)
#   x = x - 1   # один раз выведет 2

# мы можем не только уменьшать значение переменных но и увеличивать
# x = 11

# y = 0

# while x < 10:
#   x = x + 3
#   y = y + 1
#   time.sleep(1.5)
#   print("*****************")
#   print('while циркулирует ' + str(y) + ' раз')
#   print(x)
#   print("*****************")


# yazan = 1000

# month = 0

# while yazan < 10000:        # while пока у него условия true он повторяет код внутри себя
#     yazan = yazan + 1000
#     print(yazan)
#     month = month + 1
#     print(month)
#     print('язан через' + str(month) + ' месяц будет иметь' + str(yazan) + ' денег')

# print('цмко закочен')

# непонятная хуйня
# x = 0
# while x < 10:
#     if x == 5:
#         print('bmw x' + str(x))
#     x += 1
#     print(str(x) + ' x is less than 10')
# else:
# print(str(x) + ' x now is not less than 10')

# y = list(range(22, 33))
# for x in y:
#     if x == 30:
#         continue
#     print(str(x) + ' x is less than 33')
# else:
#     x += 1
#     print(str(x) + ' x now is not less than 33')


# У цикла while есть несколько ключевых слов break, continue, pass

# my_list = [1, 2, 3]

# for item in my_list:
#   pass           #если пайтон увидит pass то ему будет все равно и он пойдет дальше
# print('Another code')

# break = если пайтон увидиит break то дальше он ничего не будет делать

# continue = когда пайтон увидит continue он продолжит читать код дальше несмотря ни на что


# Тема : некоторые часто используемые фунции и операторы

# letter_index = 0
# my_string = 'dhdjdjdk'
# for letter in my_string:
#     print(letter)
#     print(letter_index)
#     print(letter + ' is at index ' + str(letter_index))
#     letter_index += 1

# в for если больше чем одно знавчение он распаковывает 
# my_string = 'dhdjdjdk'
# for index, letter in enumerate(my_string):
#     print(letter + 'is at index' + str(index)) 

#  узнать есьть ли какой то символ в слове
# print ('a' in 'jack')

#  узнать есть ли в словаре какое либо значение или ключ 
# dict_1 = {1: 'a', 2: 'b', 3: 'c'} 
# print(1 in dict_1)
# print(1 in dict_1.keys())
# print('c' in dict_1.values)

#  узнать минимальное и максимальное значение в кортеже
# print(min(1, 3, 56, 4))
# print(max(1, 3, 56, 4))

# #  узнать минимальное и максимальное значение в листе
# my_list = [1, 3, 56, 4]
# print(min(my_list))
# print(max('hello'))

# таким образом импортирется из библиотеки random функция shuffle (перемешивать значения)
# from random import shuffle
# my_list = [1, 3, 56, 4]
# shuffle(my_list)
# print(my_list) 

# #  дает рандомное число от 1 до 10 
# from random import randint 
# print(randint(1, 10))




# def = product



def product(n,func):
    result = 1
    for number in range(1,n):
        result = result + func (number)
    return result

def summ(x):
    return x+x

print (product(3,summ))
