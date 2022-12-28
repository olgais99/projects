# Работа с датами и временем. Best practices

import datetime
import pytz

# Узнаем временную разницу между странами

iso_format_string = '%Y-%m-%dT%H:%M:%S%z'

now_utc = datetime.datetime.now(pytz.timezone('UTC'))
print(now_utc.strftime(iso_format_string))

now_eu_kiev = now_utc.astimezone(pytz.timezone('Europe/Kiev'))
print(now_eu_kiev.strftime(iso_format_string))

now_eu_istanbul = now_utc.astimezone(pytz.timezone('Europe/Istanbul'))
print(now_eu_istanbul.strftime(iso_format_string))


# Вызвать все тайм зоны

# all_timezones = pytz.all_timezones
# for timezone in all_timezones:
#     print(timezone)