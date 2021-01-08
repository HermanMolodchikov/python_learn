#  https://docs.python.org/3/library/os.path.html


from datetime import date
from datetime import datetime
from datetime import timedelta
import locale


# date
today = date.today()

print(today)  # 2020-12-16
print(today.day)  # 16
print(today.month)  # 12
print(today.year)  # 2020
print(today.weekday())  # 2
print(today.ctime())  # Wed Dec 16 00:00:00 2020

# datetime

now = datetime.now()
nowToday = datetime.today()

print(now)  # 2020-12-16 16:33:47.594632
print(nowToday)  # 2020-12-16 16:33:47.594632

print(now.day)  # 16
print(now.month)  # 12
print(now.year)  # 2020
print(now.weekday())  # 2
print(now.hour)  # 16
print(now.minute)  # 39
print(now.second)  # 6
print(now.ctime())  # Wed Dec 16 16:36:17 2020

days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

print(days[now.weekday()])  # Среда

locale.setlocale(locale.LC_ALL, 'ru_RU')
print(now.strftime('%a'))  # Ср
print(now.strftime('%A'))  # среда

print(f'Date: {now.strftime("%A, %d %b %Y")}')  # Date: среда, 16 дек 2020
print(f'Time: {now.strftime("%H:%M:%S")}')  # Time: 18:22:41

print(now.strftime('%c'))  # 16.12.2020 18:23:52
print(now.strftime('%x'))  # 16.12.2020
print(now.strftime('%X'))  # 18:23:52


# timedelta

