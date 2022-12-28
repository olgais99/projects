
# try except

# try = помещаем в код который может вызвать ошибку
# except = в нем мы обрабатываем ошибку. Можно делать несколько видов except для каждой ошибки


# print('Some code')

# try:
#     print(my_variable)
#     print(len(23))

# except NameError:
#     print('Name error has happen')

# except TypeError:
#     print('Type error has happen')

# print('Code after error')


# user_dictionary = {'first_name': 'Jack', 'last_name': 'Whit', 'age': 24}

# print(user_dictionary['last_name'])
# print(user_dictionary['car'])


# В данном случае нам просто выдает что нет такого ключа

# print(user_dictionary.get('last_name'))
# print(user_dictionary.get('name'))


#  В данном случае ошибку нам не выдаст, благодаря try и except, в выводе кода с ошибкой будет просто выдавать что в ней неправильно введен ключ и при этом из за ошибки не останавливается весь код, а продолжает выводить принты

# def get_dictionary_value(dictionary, key):
#     try:
#         return dictionary[key]
#     except KeyError:
#         return None


# print(get_dictionary_value(user_dictionary, 'age'))
# print(get_dictionary_value(user_dictionary, 'a'))
# print(get_dictionary_value(user_dictionary, 'first_name'))
