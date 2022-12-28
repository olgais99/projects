
# Generator expressions Как создавать генераторы при помощи выражений генереторов

# def get_number_from_range():
#     for number in range(10):
#         yield number

# При такой записи мы можем получать по 1 числу из диапазона

# counter = get_number_from_range()
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


# Генератор созданный при помощи generator expression

# counter1 = (number for number in range(10))
# print(counter1)      #  <generator object <genexpr> at 0x7f2c000c6970>


# При такой записи мы помещаем наш диапазон чисел в список

# print([number for number in range(10)])
