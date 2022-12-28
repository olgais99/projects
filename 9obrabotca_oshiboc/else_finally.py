
# else finally

# Если мы имеем ошибку except блок срабатывает, else блок не срабатывает
# Если мы НЕ имеем ошибку else блок срабатывает, except блок не срабатывает
# Блок finally срабатывает в любом случае


# В данном случае код будет повторять строку 465 бесконечно, пока он не получить правильный ответ , то есть цифры

# while True:
#     try:
#         number = int(input('Enter some number '))
#         print(number + 2)
#     except:
#         print('You have to enter a number')
#     else:
#         print('Good Job!')
#         break
#     finally:
#         print('Finally block')

# print('Code after error handling')


# def divide(x, y):

#     try:
#         return x / y
#     except ZeroDivisionError:
#         print('You cant divide by zero')
#     except TypeError:
#         print('x and y must be numbers')
#     else:
#         print('x has devided by y')
#     finally:
#         print('finally block')


# print(divide(4, 'w'))
