
# Модуль time. Часть 1

import time

# print(time.gmtime(0))    # время с начала эпохи
# print(time.gmtime())     # текущее время
# print(time.localtime())
# print(time.time())        # сколько времени прошло с начала эпохи


# epoch_start_time = time.gmtime(0)
# print(epoch_start_time)

# print('Year: ', epoch_start_time[0])
# print('Month: ', epoch_start_time[1])
# print('Day: ', epoch_start_time[2])

# print('Year: ', epoch_start_time.tm_year)
# print('Month: ', epoch_start_time.tm_mon)
# print('Day: ', epoch_start_time.tm_mday)


# print(time.ctime(time.time()))    # показывает текущее время дату и день
# print(time.ctime(111111111111111))


# print('Text before delay')   # текст будет выходить с задержкой
# time.sleep(3.2)
# print('Text after 3.2 seconds')


# Модуль time. Часть 2

# input('Press enter to start')

# start_time = time.time()
# for i in range(1000000):
#     x = i + i
# end_time = time.time()

# # мы можем измерять промежутки времени таким образом
# print(end_time - start_time)


# Вызов текущей даты и времени

# print('Local time: ' + time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))







# Извлечение информации о timezone/ Узнаем время в разных странах
# текущее время в Киеве

import pytz
import datetime

kiev = 'Europe/Kiev'
thailand = 'Asia/Bangkok'

tz_kiev = pytz.timezone(kiev)
kiev_time = datetime.datetime.now(tz=tz_kiev)
print(kiev_time)

tz_thailand = pytz.timezone(thailand)
thailand_time = datetime.datetime.now(tz=tz_thailand)
print(thailand_time)

# Существующие тайм зоны которые мы можем использовать

# for tz in pytz.all_timezones:
#     print(tz)


# Выдает код страны, страну, список тайм зон 

for country in pytz.country_names:
    print(country, pytz.country_names[country], pytz.country_timezones.get(country))
