# Iterable & iterator

# Iterate = перебирать
# Iterable objects - те обьекты элементы которых можно перебирать. к ним относятся листы, строки, списки, словари

# number_list = [1, 2, 3, 4, 5]

# for number in number_list:
#     print(number)

# for letter in 'my string':
#     print(letter)


# Iterators
#  Функция iter  = мы можем передавать нашу переменную

# number_list_iterator = iter(number_list)
# print(type(number_list_iterator))

# string_iterator = iter('my_string')
# print(type(string_iterator))


# Вызов метода __next__ Перебираем из нашей переменной цифры, пока не закончаться цифры будет выводится код, потом выведется StopIteration

# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())


# print(string_iterator.__next__())
# print(string_iterator.__next__())


# # Можно перебирать через функцию next

# print(next(number_list_iterator))
# print(next(number_list_iterator))
# print(next(number_list_iterator))


# Используем цикл while чтобы оно перебирало до тех пор пока не переберет все буквы или цифры

# def my_for_loop(iterable):
#     iterator = iter(iterable)

#     while True:
#         try:
#             print(iterator.__next__())
#         except StopIteration:
#             print('Iteration is finished')
#             break


# my_for_loop('hello')
# my_for_loop([1, 1, 2, 3])
