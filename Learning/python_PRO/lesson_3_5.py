import sys
from datetime import datetime, timedelta


def str2datetime(dt: str) -> datetime:
    return datetime.strptime(dt, '%d.%m.%Y %H:%M')


def choose_plural(amount: int, declensions: tuple):
    if int(str(amount)[~1:]) not in [11, 12, 13, 14]:
        l = [[1], [2, 3, 4], [5, 6, 7, 8, 9, 0]]
        for i in range(3):
            if int(str(amount)[~0]) in l[i]:
                return f"{amount} {declensions[i]}"
    return f"{amount} {declensions[2]}"


def timedelta2str(td: timedelta) -> str:
    days = choose_plural(td.days, ('день', 'дня', 'дней'))
    hours = choose_plural(td.seconds // 3600, ('час', 'часа', 'часов'))
    minutes = ('минута', 'минуты', 'минут')
    return f"{days} {hours}"


start_date = str2datetime('08.11.2022 12:00')
today_date = str2datetime(input())
print(start_date)
print(today_date)
print(f'До выхода курса осталось: {timedelta2str(start_date - today_date)}')


sys.exit(999)

def str2datetime(dt: str) -> datetime:
    return datetime.strptime(dt, '%d.%m.%Y')


def datetime2str(dt: datetime) -> str:
    return dt.strftime('%d.%m.%Y')


def check_parity(dtm: datetime) -> bool:
    return bool((dtm.day + dtm.month) % 2)


def check_weekday(dtm: datetime) -> bool:
    return dtm.weekday() not in (0, 3)


def date_range(start: datetime, end: datetime) -> list:
    dates = [start + timedelta(days=i) for i in range((end - start).days)] + [end]
    if not check_parity(dates[0]):
        dates = dates[1:]
    dates = [datetime2str(dtm) for dtm in dates if not (dates.index(dtm) % 3) and check_weekday(dtm)]
    print(*dates, sep='\n')


date_range(str2datetime('01.11.2021'), str2datetime('10.11.2021'))
