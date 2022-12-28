
# #  встроенные фунции
# x = print('hello')
# y = set()

# print(type(x))
# print(type(y))


# фунции создаются при помощи ключевого слова def. круглые скобки означают функцию
# def print_greting():
#     print('hello')
# print_greting()

#!  фкнкции созжаются таким образом: пишется def, дальше пишется названи е фкнкции, ставятся круглые скобки и если нам нужно ставить какие то переменные они ставятся в эти крглые скобки (если нам нужно задать парамент по умолчанию мы пише название переменной = и наше значение по умолчанию). после того как мы создали переемннную мы можем написать и описание. это делается в многострочном омментарии в начале функции. функции могут что то возращать а могут работать непострелственно с кодом. Функции вызываются таким образом: название фкнции и кругоые скобки
def print_greeting__name(name = 'Olga'):
    '''
    сдесь должно быть описание фкнуции
    :param name
    :return: None
    '''
    print('hello' + name + '!')


print_greeting__name(' olga')


# help(print_greeting__name)


# def sum_of_two_numbers(a = 0, b = 0):
#     '''
#     :param a :
#     :param b :
#     :return:
#     '''
#     c = a + b
#     return c


# sum_of_two_numbers()
# print(sum_of_two_numbers())


# x = sum_of_two_numbers(1, 1)
# print(x)
# help(sum_of_two_numbers)


# def x(olga = 22,yazan = 23):


#     age_Olga = 2022 - olga
#     ageYazan = 2022 - yazan


#     list_which_year = [age_Olga,ageYazan]


#     return list_which_year


# x = list_which_year


# def yazan (batery, usb, mouse):

#     batery_mouse = batery + usb + mouse

#     return batery_mouse

# yazan_return = yazan('panasonic', '2.4', 'gamebeard' )
# print(yazan_return)


# yazan = '15000'
# olea = '10000'


# cashilec = 0


# def calculete_and_take_in_cashilec(x, y):
#     cashilec = x + y


# calculete_and_take_in_cashilec(yazan, olea)

# print(cashilec)


# # ! *args это котреж в который будет записано все что мы поставим в фкнуцию 
# def magazin (*args):
#     money = 0
#     for item in args:
#         money = money + item 
#     return money 



# money_for_magazin = magazin (24, 10, 50, 100, 100, 84, 98)
# print(money_for_magazin)


#  первым значением мы вставляем цену евро, а все остальное это наши комунальные 
# def uslugi (euro, *args):
#     money = 0  
#     for item in args:
#         money = money + item 
#     itog = money / euro 
#     return itog 



# comunalka = uslugi (19, 200, 800)
# print(comunalka)

# #! *args      (1, 2, 3)
# def func_with_args(*args):
#     print(args)

# func_with_args(1, 2, 3)



# #! **kwargs     {'first': 1, 'second': 2, 'third': 3}
# def func_with_kwards(**kwargs):
#     print(kwargs)

# func_with_kwards(first=1, second=2, third=3)



# ! их можно использовать вместе
# def func_with_args_and_kwargs(*args, **kwargs):
#     print(args)
#     print(kwargs)


# func_with_args_and_kwargs('one', 'two', 3, drink='cofe', eat='soup')


