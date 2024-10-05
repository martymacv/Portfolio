import calendar
import sys
from datetime import datetime, timedelta


numbers = [-214, 777, 181, 9, 32, -139, 43, 89, 77, 448, -20, -917, 54, 5, 432, 43, 32, 422, -895, 7, 198, 284, 472, 3, -986, -964, -989, 29]

numbers.remove(3)
numbers.remove(5)
numbers.remove(7)
numbers.remove(9)
print(numbers)


numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
numbers.insert(4, 111)
print(numbers)



top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
top[~0] = "Сверхъестественное"
top[2] = "Настоящий детектив"
print(top)


def datetime2str(dt: datetime) -> str:
    return dt.strftime('%d.%m.%Y')


def date_range(year: int) -> list[datetime]:
    return [the_third_thursday_in_month(datetime(year=year, month=i + 1, day=1)) for i in range(0, 12)]


def the_third_thursday_in_month(dt: datetime) -> datetime:
    day = dt.day
    while calendar.weekday(year=dt.year, month=dt.month, day=day) != 3:
        day += 1
    day += 14
    return dt.replace(day=day)


def get_all_mondays(year: int) -> list[str]:
    return list(map(datetime2str, date_range(year)))


print(*get_all_mondays(2021), sep='\n')
print([1] * 77)
sys.exit(999)

def str2date(year: int, month: int, day: int) -> date:
    return date(year=year, month=month, day=day)


def list_concat(lst: list) -> list:
    output = []
    for el in lst:
        output += el
    return list(sorted(set(output)))[1:]


def get_days_in_month(year: int, month: str):
    month = list(calendar.month_name).index(month)
    return list(map(lambda day: str2date(year, month, day), list_concat(calendar.monthcalendar(year, month))))


print(get_days_in_month(2021, 'December'))

sys.exit(999)
year, month = [x for x in input().split()]
print(calendar.monthrange(int(year), list(calendar.month_name).index(month))[1])
