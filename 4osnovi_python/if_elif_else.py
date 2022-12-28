# Условный оператор if elif else. Условные операторы нужны для того чтобы выполнять тот или иной код на основе вычисления результата boolean выражения, которое возвращает значение true или false


# yazan = 130
# if yazan >= 160:                    # если
#     print('mackdonalds')
# elif yazan >= 15 and yazan < 160:   # или же
#     print('coffe')
# else:                            # в противном случае
#     print('nahui')

# x = 4
# if x > 3:   #если х больше 3 :
#    print('x > 3') #с отступом код который будет выполняться если х больше 3

# elif x <3:   #иначе если х меньше 3
#   print('x < 3')
# else:            # иначе, выполнется в том случае когда предыдущие ветки не срабатывают
#    print('x == 3')

# Отступы важны, тот блок кода который выполняется при истинности условия должен идти с отступом


# day_time = 'night'  # если в переменную написать значение которое не существует то срабатывает последний оператор else

# if day_time == 'morning':
#    print('Monster wakes up')
# elif day_time == 'afternoon':
#    print('Monster is walking')
# elif day_time == 'evening':
#    print('Monster is eating ')
# elif day_time == 'night':
#    print('Monster is sleaping')
# else:
#   print('Monster is doing something')
# Выводит Monster is walking

# Мы можем использовать этот оператор не полностью, можем показать только часть if
# x = 50
# if x % 2 == 0:
#   print('x is even')  # x четное
# else:   # можно поместить только 1 условное слово в операторе
#   print('x is odd')   # x нечетное

#   # Значения сами по себе могут быть правдивыми или лживыми
# if 56:       #код ничего не выводит, потому что значение 0 ложно , расценивается как ложь всегда. Еси поставим любое другое число то код выведет значение, любая другая цифра расценивается как правда
#     print('something')

#  if '':   # В строках пустая строка тоже имеет значение ложь
# print('something')

# if None:     # если мы укажем значение none = пустота, тоже расценивает как ложь и ничего не выводит
# print('something')

# lucky_number = int(input ('Enter a number  '))
# if lucky_number:    #если пользователь ввел что то, тогда мы выводим следующий текст
#   print(lucky_number + '  is your lucky number')
# else:       # если пользователь не ввел ничего, тогда мы выводим следующий код
#   print('you have to enter some number, please try again')
