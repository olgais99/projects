# Лямбда выражения

# Лямбда выражения =  это быстрый способ для создания анонимных функции. это такая функция которая используется 1 раз в момент ее создания, мы больше не можем ее где то использовать и вызывать.

#  Встроенная функция map

# def sum_of_two_numbers(x):
#     return x + x


# sum_of_two_numbers('olga')
# print(sum_of_two_numbers('olga'))
# print(sum_of_two_numbers('yazan'))
# print(sum_of_two_numbers(2))
# print(sum_of_two_numbers('olge nado povtoreati vseo po 2 raza,  '))


# number_list = [1, 2, 3, 4, 6, 7]

# result = map(sum_of_two_numbers, number_list)
# print(result)

# # # результат <map object at 0x7f9e8c67f340> обьект типа мэп по адресу в памяти компьютера

# # # из этого результата мы можем получить наши цифры через цикл

# for item in map(sum_of_two_numbers, number_list):
#     print(item)

# # #  мы можем получать результат через список
# print(list(map(sum_of_two_numbers, number_list)))


# def is_a_in_string(string):
#     '''
#     эта функция ожиэает 1 обязательный элемент в типе данных list в котором будет string
#     '''
#     if 'a' in string:
#         print('String has "a"')
#         return True     # возвращает список из значений которая возвращает эта функция
#     else:
#         return False
#         print('String has not "a"')


# string_list = [
#     'hi', 'was', 'name', 'he'
# ]

# print(list
#       (
#           map
#           (
#               is_a_in_string, string_list
#           )))


#   Встроенная функция filter  = эта функция работает только с функциями которые возвращают правду или ложь и на основании булин значения она извлекает из последовательности элемент который при применнеи в функции возвращает правду

# def is_number_odd(number):
#   return number % 2 == 1

# number_list = [1, 2, 3, 4, 6, 7]


# print(filter(is_number_odd, number_list))
# # #  результат <filter object at 0x7f4564e17340>

# print(list((is_number_odd, number_list)))
# # результат [1, 2, 3, 4, 6, 7]


# def is_a_in_string(string):
#     if 'a' in string:
#         print('String has "a"')
#         # возвращает список из значений которая возвращает эта функция ['was', 'name']
#         return True
#     else:
#         return False
#         print('String has not "a"')


# string_list = ['hi', 'was', 'name', 'he']

# print(list(filter(is_a_in_string, string_list)))


#  Лябмда выражения используется для создания анонимных функций

def cube(number):
  return number * 2


# number_list = [1, 2, 3, 4, 6, 7]
# print(list(map(lambda number: number ** 3, number_list)))


# print(cube(2))


one = lambda number: number * 2 

print(cube(2))

print(one(2))