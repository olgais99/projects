# # Boolean значения = True = False, пишутся только с большой буквы
# print(1 < 2)
# print(type(True))   #<class 'bool'>
# print(type(False))

# # Какие бывают операторы сравнения 
# # оператор равенство ==
# print(1 == 1) 
# print(1 == 2)
# print('hello' == 'hello')
# print('hello' == 'Hello')

# # оператор не равно !=
# print(1 != 1) 
# print(1 != 2) 
# print('hello' != 'hello')
# print('hello' != 'Hello')

# оператор больше >
# print(1 > 2) 
# # оператор меньше <
# print(1 < 2) 
# # оператор больше либо равно (>=), оператор меньше либо равно(<=)
# print(2 >= 2)
# print(3 <= 2)

# Сравниваем строки, строки сравниваются посимвольно, нет отдельного типа данных для символов. У каждого символа есть свой ASCII код = это числовой код для каждого символа
# Мы можем узнать код при помощи функции ord 
# print(ord('a'))    #97
# print(ord('b'))    #98
# print('a' > 'b')
# print('hi' > 'hello') #True
# print(ord('i'))    #105
# print(ord('e'))    #101

# Мы можем присваивать значения переменым и сравнивать переменные
# x = 10
# y = 23
# print(x > y)
# print(x < y)
# print(x == y)
# print(x != y)

#  input это функция для взаимодействия с пользвателем, присваивая функцию input к переменной мы можем хранить то что напимсал пользователь, в круглых скобках inputа мы можем написать человеку подстказку, эта фкнуиця всегда возращает string
# age = input('Input your age')
# print('Your age is' + (age)) # далее в самом коде пишем 45 лет и нажимаем enter 

# # Если у нас есть возраст пользователя больше 18 то мы разрешаем вход, если меньше 18 то доступ запрещен
# age = int(input('Input your age     '))
# print('Access is permitted: ' + str(age >= 18)) 

# 
# text = int(input('Введите число '))
# print(type(text))


# ДЗ
# olga = 23
# yazan = 30

# print(olga == yazan)
# print(olga != yazan)
# print(olga > yazan)
# print(olga < yazan)
# print(olga <= yazan)


# print('o' > 'O')
# print(ord('o'))
# print(ord('O'))


print(1==True)