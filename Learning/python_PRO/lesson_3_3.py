import sys
from datetime import date, time, datetime, timedelta


schedule = [('9:00', '21:00'),
            ('9:00', '21:00'),
            ('9:00', '21:00'),
            ('9:00', '21:00'),
            ('9:00', '21:00'),
            ('10:00', '18:00'),
            ('10:00', '18:00')]


def str2datetime(tm: str, tp: int) -> datetime:
    patterns = ['%d.%m.%Y %H:%M',
                '%H:%M:%S',
                '%H:%M']
    return datetime.strptime(tm, patterns[tp])


def is_open(schdl: list, dtm: datetime) -> any:
    dt, tm = str2datetime(schdl[dtm.date().weekday()][1], 2), str2datetime(str(dtm.time()), 1)
    return ('Магазин не работает', (dt - tm).seconds // 60)[dt >= tm]


print(is_open(schedule, str2datetime('02.11.2021 21:15', 0)))


sys.exit(999)
def str2datetime(dt: str) -> datetime:
    return datetime.strptime(dt, '%d.%m.%Y')



def datetime2str(tm: datetime, tp: int) -> str:
    patterns = ['%d.%m.%Y %H:%M',
                '%H:%M']
    return tm.strftime(patterns[tp])


days = [0, 0, 0, 0, 0, 0, 0]
for year in range(1, 10000):
    for month in range(1, 13):
        days[datetime(year=year, month=month, day=13).weekday()] += 1


print(*days, sep='\n')



sys.exit(999)
data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]


def str2datetime(time: str) -> datetime:
    return datetime.strptime(time, '%H:%M')


def print_total_minutes(dates: list) -> None:
    print(sum([(str2datetime(end) - str2datetime(start)).seconds for start, end in dates]) // 60)


print_total_minutes(data)


sys.exit(999)

from datetime import datetime, timedelta


def str2list(dates: str) -> list:
    return list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), dates.split()))


def make_diffs(dates: str) -> list:
    dts = str2list(dates)
    return [abs((dts[i] - dts[i - 1]).days) for i in range(1, len(dts))]


# INPUT DATA:

# TEST_1:
print(make_diffs('05.10.2021 06.10.2021 07.10.2021 08.10.2021 09.10.2021'))

# TEST_2:
print(make_diffs('06.10.2021 05.10.2021 08.10.2021 09.10.2021 07.10.2021'))

# TEST_3:
print(make_diffs('05.10.2021'))

# TEST_4:
print(make_diffs('05.10.2021 05.10.2021 05.10.2021 05.10.2021 05.10.2021'))

# TEST_5:
print(make_diffs('02.01.2021 10.11.2021 13.07.2021 14.05.2021 16.06.2021'))

# TEST_6:
print(make_diffs('02.01.2018 10.11.2019 13.07.2020 14.05.2021 16.06.2022'))

# OUTPUT DATA:

# TEST_1:
[1, 1, 1, 1]

# TEST_2:
[1, 3, 1, 2]

# TEST_3:
[]

# TEST_4:
[0, 0, 0, 0]

# TEST_5:
[312, 120, 60, 33]

# TEST_6:
[677, 246, 305, 398]

sys.exit(999)
# символы - воскресенья в году (комбинации год + месяц + день)
# алфавит - воскресенья в выбранном году (множество)


def year2datetime(year: int, month: int, day: int) -> datetime:
    return datetime(year=year, month=month, day=day)


def num_of_sundays(year: int) -> int:
    start = datetime(year=year, month=1, day=1)
    end = datetime(year=year, month=12, day=31)
    prep_step = 7 - start.isoweekday()
    start += timedelta(days=prep_step)
    return (end - start).days // 7 + 1           # +1, потому что точек на отрезке всегда на 1 больше, чем промежутков между точками



# INPUT DATA:

# TEST_1:
print(num_of_sundays(2021))

# TEST_2:
year = 2000
print(num_of_sundays(year))

# TEST_3:
print(num_of_sundays(768))

# TEST_4:
print(num_of_sundays(1944))

# TEST_5:
print(num_of_sundays(2022))

# TEST_6:
print(num_of_sundays(2050))

sys.exit(999)
dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)

print(dt.strftime('%d.%m.%Y %H:%M:%S'))

today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = birthday - today

print(type(days.days))

print((datetime.strptime('00:01:01', '%H:%M:%S') - datetime.strptime('00', '%S')).seconds)




sys.exit(999)
# алфавит - это набор дат, то есть символ это 01.11.2021
# строка - это диапазон дат, то есть 05.11.2021-09.11.2021, слова не могут быть больше 2-х символов и могут соединяться только знаком "-"
# предложение - это список строк или список слов, которые могут состоять или из 1 символа или из 2-х


def str2datetime(values: list) -> list:
    return [datetime.strptime(value, '%d.%m.%Y') for value in values]


def str2char(value: str) -> list:
    if '-' not in value:
        value += '-' + value
    return value.split('-')


def check_intersection(checked_dates, date_for_checking):
    return checked_dates[1] < date_for_checking[0] or checked_dates[0] > date_for_checking[1]


def is_available_date(booked_dates: list, date_for_booking: str):
    check_list = []
    for dt in booked_dates:
        check_list.append(check_intersection(str2datetime(str2char(dt)), str2datetime(str2char(date_for_booking))))
    return all(check_list)


# INPUT DATA:

# TEST_1:
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))

# TEST_2:
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

# TEST_3:
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))

# TEST_4:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '12.11.2021'
print(is_available_date(dates, some_date))

# TEST_5:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '09.11.2021'
print(is_available_date(dates, some_date))

# TEST_6:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '15.11.2021'
print(is_available_date(dates, some_date))

# TEST_7:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '17.11.2021'
print(is_available_date(dates, some_date))

# TEST_8:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '22.11.2021-25.11.2021'
print(is_available_date(dates, some_date))

# TEST_9:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

# TEST_10:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '02.11.2021-05.11.2021'
print(is_available_date(dates, some_date))

# TEST_11:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '10.11.2021-14.11.2021'
print(is_available_date(dates, some_date))

# TEST_12:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '03.11.2021-05.11.2021'
print(is_available_date(dates, some_date))

# TEST_13:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '09.11.2021-10.11.2021'
print(is_available_date(dates, some_date))

# TEST_14:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '06.11.2021-08.11.2021'
print(is_available_date(dates, some_date))

# TEST_15:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '14.11.2021-22.11.2021'
print(is_available_date(dates, some_date))

# TEST_16:
dates = ['14.09.2022-14.10.2022']
some_date = '20.09.2022'
print(is_available_date(dates, some_date))

# TEST_17:
dates = ['14.09.2022-14.10.2022']
some_date = '14.11.2022'
print(is_available_date(dates, some_date))

# TEST_18:
dates = ['14.09.2022-14.10.2022']
some_date = '15.11.2022-16.11.2022'
print(is_available_date(dates, some_date))

# TEST_19:
dates = ['14.09.2022-14.10.2022']
some_date = '14.09.2022-22.09.2022'
print(is_available_date(dates, some_date))

# TEST_20:
dates = ['02.11.2021', '05.11.2021-09.11.2021']
some_date = '04.11.2021'
print(is_available_date(dates, some_date))

# OUTPUT DATA:
True
False
False
False
False
False
False
True
False
False
False
False
False
False
False
False
True
True
False
True
sys.exit(999)

diary = dict()
with open("diary.txt", "r", encoding="utf-8") as f_in:
    records = f_in.read().split('\n\n')
    for record in records:
        dtm = record.split('\n')
        dt, tm = dtm[0].split('; ')
        diary[datetime.strptime(dt + tm, '%d.%m.%Y%H:%M')] = record
        # print(dt, tm)
        # print(dtm[1:])

for dtm in sorted(diary):
    print(diary[dtm])
    print()

sys.exit(999)

data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
        'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
        'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
        'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
        'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
        'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
        'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
        'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
        'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
        'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
        'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}

pattern = '%d.%m.%Y %H:%M:%S'
for student, tm in data.items():
    data[student] = datetime.strptime(tm[1], pattern).timestamp() - datetime.strptime(tm[0], pattern).timestamp()

print(min(data.items(), key=lambda x: x[1])[0])

dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
         date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
         date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]

times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
         time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
         time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]

datetimes = []
for dt, tm in zip(dates, times):
    datetimes.append(datetime.combine(dt, tm))

print(*sorted(datetimes, key=lambda x: x.second), sep='\n')

times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
                      datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
                      datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
                      datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
                      datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
                      datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
                      datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
                      datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
                      datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
                      datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
                      datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
                      datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
                      datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
                      datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]

noon = time(12, 0, 0)
noons = [0, 0]
for tm in times_of_purchases:
    noons[tm.time() > noon] += 1
print(("После полудня", "До полудня")[noons[0] > noons[1]])


seconds = 2483228800
dt = datetime(2011, 11, 4)

print(datetime.fromtimestamp(seconds))
print(dt.timestamp())