
# Модуль datetime. Класс timedelta  = представлет из себя промежуток времени, Разницу между 2 датами

from datetime import timedelta, datetime

year = timedelta(days=365)
print(year)

# Узнаем через поставленное колво дней какая будет дата

# today = datetime.now()
# print('Today is', today)
# print('23 days from today will be', (today + timedelta(days=23)))
# print('230000 seconds from today will be', (today + timedelta(seconds=230000)))


# Узнать сколько дней назад был мой др

today = datetime.now()
last_birthday = datetime(2022, 11, 12)
print('My last birthday was {0} days ago.'.format((today - last_birthday).days))

# Узнать сколько секунд в году

year = timedelta(days=365)
print('There are {0} seconds in a year.'.format(year.total_seconds()))