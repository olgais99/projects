# Модуль datetime. Класс date

from datetime import date

# # Отображает текущую дату = 2022-12-07

# today = date.today()
# print(today)

# print(today.year)   # отдельно выдает год, месяц и дату
# print(today.month)
# print(today.day)


# Узнать разницу между периодами времени

# date_1 = date(2022, 12, 7)
# date_2 = date(2021, 12, 7)
# diff = date_1 - date_2
# print(diff)

# print(type(date_1))
# print(type(date_2))
# print(type(diff))


# today = date.today()
# print(today)

# my_birthday = date(2023, 11, 12)
# my_birthday_1 = date(2022, 12, 7)

# days_until_birthday = my_birthday - my_birthday_1
# print('You will celebrate your birthday in' , days_until_birthday.days, 'days!')    # атбрибут .days выдает только дни, без времени


# Вывести какой день недели

# today = date.today()
# week_day = today.weekday()
# print(week_day)


# Создаем программу чтобы пользователь мог узнать по датам какой день недели был или будет.

year = input('Please enter a year ')
month = input('Please enter a month ')
day = input('Please enter a day ')

date_1 = date(int(year), int(month), int(day))
# print(date_1)

week_day = date_1.weekday()

if week_day == 0:
    print(date_1, 'is a Monday.')
elif week_day == 1:
    print(date_1, 'is a Tuesday.')
elif week_day == 2:
    print(date_1, 'is a Wednesday.')
elif week_day == 3:
    print(date_1, 'is a Monday.')
elif week_day == 4:
    print(date_1, 'is a Thursday.')
elif week_day == 5:
    print(date_1, 'is a Friday.')
elif week_day == 6:
    print(date_1, 'is a Saturday.')
elif week_day == 7:
    print(date_1, 'is a Sunday.')
