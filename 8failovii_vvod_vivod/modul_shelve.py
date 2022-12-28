#  Модуль shelve представляет собой хранение данных на подобе словаря, но в отличии от словаря данные хранятся в файле, ключи должны быть обязательно строками.


# import shelve

# with shelve.open('shelve_test') as cars:
#     cars['opel'] = 'Germany'
#     cars['ford'] = 'USA'
#     cars['mazda'] = 'Japan'
#     cars['renault'] = 'France'

#     print(cars['ford'])
#     print(cars['renault'])


# # как распечатать ключи

# import shelve
# for key in cars:
#     print(key)


# Работа с данными при помощи модуля shelve

# Выводить по названию машины в коде страну производства

# while True:
#     key = input('Please enter a car name: ')
#     if key == 'quit':
#         break
#     country = cars.get(key)
#     print(country)

# Выводить по названию машины в коде страну производства, если такой машины нет оно выведет что данной марки нет

# while True:
#     key = input('Please enter a car name: ')
#     if key == 'quit':
#         break
#     if key in cars:
#         country = cars[key]
#         print(country)
#     else:
#         print('We dont have a ' + key)


#  Как распечатать все значения

# for value in cars.values():
#     print(value)
#     print(cars.values)


# Обновление данных при помощи модуля shelve

# import shelve

# monday_schedule = ['Math', 'English', 'Python', 'Football']
# tuesday_schedule = ['English', 'HTML', 'Python', 'Football']
# wednesday_schedule = ['Physics', 'English', 'Python']
# thursday_schedule = ['Math', 'Chemistry', 'Python']
# friday_schedule = ['Russian', 'Java', 'Running']


# with shelve.open('schedule') as schedules:
#     schedules['monday_schedule'] = monday_schedule
#     schedules['tuesday_schedule'] = tuesday_schedule
#     schedules['wednesday_schedule'] = wednesday_schedule
#     schedules['thursday_schedule'] = thursday_schedule
#     schedules['friday_schedule'] = friday_schedule


# # Как добавить в расписание урок

#     temp_list = schedules['thursday_schedule']
#     temp_list.append('Swimming')
#     schedules['thursday_schedule'] = temp_list


#     for key in schedules:
#         print(key, schedules[key])


# Конвертация словаря в объект shelve


# import shelve

# university = shelve.open('university_file')
# university['schedules'] = {

#     'monday_schedule': ['Math', 'English', 'Python', 'Football'],
#     'tuesday_schedule': ['English', 'HTML', 'Python', 'Football'],
#     'wednesday_schedule': ['Physics', 'English', 'Python'],
#     'thursday_schedule': ['Math', 'Chemistry', 'Python'],
#     'friday_schedule': ['Russian', 'Java', 'Running']
# }

# university['tutors'] = {
#     'Math': ['Jack White', 'Jim Black'],
#     'Python': ['Yazan Darwish', 'Jane Smith']
# }


# print(university['schedules']['wednesday_schedule'])
# print(university['tutors']['Math'])


# university.close()

# Теперь мы все получаем через обьект shelve
