# # Tuples = кортеж (указывается в скобках), можно указывать без скобок, но лучше всегда использовать скобки чтобы было понятнее. Tuple - Неизменяем как и строка
# tuple_1 = 1, 2, 3
# # # # Можем вывести type и узнать какой класс если нам непонятен какой класс
# # print(type(tuple_1))

# tuple_2 = ('one', 'hello')
# tuple_3 = (3, 2.3, 'three')
# # для того чтобы вывести элемент кортежа еам нужно в квадратных скобках вписать его индекс
# print(tuple_1[1])
# # print(tuple_2)
# # print(tuple_3)

# # так как кортеж неизменный мы можем только создать новый кортеж заполняя его нужными элементами старого кортэжа и вручную вписать нужные элемента. 
# new_tuple = (tuple_1[0], 3, tuple_1[2])
# print(new_tuple)

# Структура Tuple позволяет данные целостными 

# # Распаковка данных в Tuple
# x = y = z = 12
# # # Множественное присваивание в одной строке
# x, y, z = 12, 13, 14
# print(x, y, z)

# # Распаковка обьекта Tuple в переменную. Данные извлекаем из обьекта Tuple в переменную 
# person_tuple = ('John', 'Smith', 1986)
# first_name, last_name, year_of_birth = person_tuple
# print(first_name, last_name, year_of_birth)

# # Метод count = показывает сколько раз повторяется одно и тоже значение
# t1 = (5, 2, 1, 1, 7, 9)
# print(t1.count(1))
# # Тот же метод можно использовать и со строками 
# greetings_tuple = ('hello', 'hi', 'hey', 'hi')
# print(greetings_tuple.count('hi'))

# # МЕТОД index, можно вычислить индекс какого то элемента, выдает 1 индекс встречающегося элемента. Если нам надо извлечь индексы всех одинаковых элементов мы можем использовать программную структуру цикл, но это будет рассматриватся в други уроках 
# print(t1.index(5))
# print(greetings_tuple.index('hey'))

# Д/З
# computer = ('Notebook', 'Macbook Pro', 'silver', 2017 )
# computer_type, model, color, year = computer
# print(computer_type, model, color, year)




