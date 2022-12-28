
# # для того чтобы из типа данных integer превратить в тип данных string мы должны воспользоваться функцикй str()
# print(1 + 1)
# print ('1'+ '1')
# age = 23
# print('Jack is ' + str(age) + 'years old.' )
# print('Jack is ' + str(23) + 'years old.' ) 

# # функция format заполняет плейс холдеры в строке своими значениями
# name = 'Jack'
# age = 23
# color = 'black'
# name_and_age = 'My name is {0}. I\'m {1} years old. I\'m {2} '.format(name, age, color) 
# print(name_and_age)

# week_days = 'There are 7 days in a week: {6}, {5}, {4}, {3}, {2}, {1}, {0}.'.format("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# print(week_days)

# # в плейс холдеры вставляем индексы в виде включей который стоят после format mo=monday значит в плэйс холдер {mo}
# week_days_1 = 'There are 7 days in a week: {mo}, {tu}, {we}, {th}, {fr}, {sa}, {su}'.format(mo ='Monday', tu = 'Tuesday', we = 'Wednesday', th = 'Thursday', fr = 'Friday', sa = 'Saturday', su = 'Sunday')
# print(week_days_1)


# форматиируем количество символов после точки {0 это индекс:1 это количество всех символов в числе.3f это нужное колво символов после точки f это флоат}
# float_result = 1000/7
# print(float_result)
# print('The result of division is {0:1.3f}'.format(float_result))

# #вывести числа в виде таблицы {индес : сколько знаков хотим выделить. сколько знаков после запятойf}
# print('''
# {0:10.2f} {1:10.2f} {2:10.2f}
# {3:10.2f} {4:10.2f} {5:10.2f}
# {6:10.2f} {7:10.2f} {8:10.2f}
# '''.format(1.45778, 343.232352, 34.2344, 1234.23,
# 1.45778, 343.232352, 34.2344, 1234.23,
# 456.43234))


name = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\'m {1} years old'.format(name, age) 
print(name_and_age)
# не указывать в конце формат = просто в начале указать букву f и в плэйс холдеры пишем значения
name_and_age = f'My name is {name}. I\'m {age} years old'.format(name, age) 
print(name_and_age)