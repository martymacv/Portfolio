# импортируем тип date из модуля datetime
from datetime import date, timedelta

# создаем объект, соответсвующий дате урагана
hurricane_andrew = date(1992, 8, 24)

# выводим день недели
print(hurricane_andrew.weekday())

dt = date.today()
print(dt.month)

# from datetime import date

dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]

for dt in dates:
    print(f"{dt}  {dt.year}-Q{int(dt.month // 3 + (dt.month % 3 != 0))}")


# from datetime import date


def get_date_range(start: date, end: date) -> list:
    dates = []
    while start <= end:
        dates.append(start)
        start += timedelta(days=1)
    return dates

date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')


def saturdays_between_two_dates(start: date, end: date) -> int:
    saturdays = []
    borders = sorted([start, end])
    while borders[0] <= borders[1]:
        if borders[0].isoweekday() == 6:
            saturdays.append(borders[0])
        borders[0] += timedelta(days=1)
    return len(saturdays)


date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))