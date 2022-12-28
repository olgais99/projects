# # # Логические операторы системы языка пайтон
# x = 1
# y = 2

# # print(x > 1)
# # print(y > 1)

# # # # Существуют 3 основных логических оператора = and, or, not
# print(x > 1 and y > 1)  # чтоб получить права нам нужно сдать теорию и практику  # мы хотим чтобы и х был больше 1, и у больше 1
# print(x > 1 or y > 1)  # оплатить в магазине покупку можем или через карту или кеш
# print(not  x > 1) # не х больше 1
# print(not  y > 1) # не y больше 1

# print(True and True)   #True если справа и слева true то ответ будет true
# print(True or True)    #True если справа true а слева false то ответ будлет false
# print(not True)        #False

# print(False and False)  #False
# print(False or False)  #False
# print(not False)       #True

# print(True and False)   #False
# print(True or False)  #True

# # На сайте знакомств у нас есть данные пользователя
# name = 'John'
# age = 45
# is_married = False  # переменная для хранения boolean значения ( оздается при помощи задавания вопроса на который можно ответить истина или ложь)

# #if оператор = этот условный оператор действует на основании вычисления истина ли значение этого выражения
# if age > 18 and is_married == False:   #если больше 18 и он не женат
#     print('Hi {}, You can find a girl of your dream here'.format(name))

# age_of_person = int(input('input your age '))
# print('acces is permited: ' + str(age_of_person >= 18))
