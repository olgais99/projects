# Generator functions
# При помощи generator мы можем перебирать итераторы
# Генераторы могут быть созданы при помощи функции генераторов, а так же могут быть созданы при помощи генераторов выражений

# def my_function(x):
#   return x

# print(my_function(4))

# Когда мы употребляем в функции ключевое слово yield, автоматические мы получаем из этой функции генератор

# def count_up_to(x):
#     count = 1
#     while count <= x:
#         yield count
#         count += 1


# print(count_up_to(4))

# counter = count_up_to(4)
# print(counter.__next__())

# counter = count_up_to(10)


# Выдает последовательность из чисел до 10, включая 10

# for number in count_up_to(10):
#     print(number)
