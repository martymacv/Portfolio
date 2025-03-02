import csv
import sys
from datetime import datetime
import time


# у меня есть таблица и в ней нужно найти все строки с минимальной ценой на продукт


def filter_by_row(row: dict) -> tuple:
    return list(row.items())[0], min(list(row.items())[1:], key=lambda x: int(x[1]))


def filter_by_column(fields: list) -> list:
    min_price = min(fields, key=lambda x: int(x[1][1]))[1][1]
    return sorted(list(map(lambda x: (x[1], x[0]), filter(lambda y: y[1][1] == min_price, fields))))


with open('prices.csv', 'r', encoding='utf-8') as csv_file:
    data = csv.DictReader(csv_file, delimiter=';')
    product_name, shop_name = filter_by_column(list(map(filter_by_row, list(data))))[0]
    sys.stdout.writelines(': '.join([product_name[0], shop_name[1]]))


sys.exit(999)
def sorted_by_fieldnames(row: dict) -> dict:
    first_column = list(row.items())[0]
    other_columns = list(row.items())[1:]
    return dict([first_column] + sorted(other_columns, key=lambda x: (int(x[0][0: x[0].index('-')]), x[0][x[0].index('-') + 1:])))


with open('student_counts.csv', encoding='utf-8') as csv_read, \
        open('sorted_student_counts.csv', 'w', encoding='utf=8', newline='') as csv_write:
    data = csv.DictReader(csv_read)
    sorted_data = list(map(sorted_by_fieldnames, list(data)))
    writer = csv.DictWriter(csv_write, fieldnames=sorted_data[0])
    writer.writeheader()
    writer.writerows(sorted_data)

sys.exit(999)


def group_by_id_name(table: list) -> dict:
    dict_out = dict()
    for id, prop, value in table:
        dict_out[id] = dict_out.get(id, dict())
        dict_out[id][prop] = value
    return dict_out


def unpack2table(group_table: dict, id_name: str) -> list:
    table = list()
    for key, value in group_table.items():
        header = {id_name: key}
        header.update(value)
        table.append(header)
    return table


def condense_csv(filename: str, id_name: str) -> list:
    with open(filename, 'r', encoding='utf-8') as csv_read, \
            open('condensed.csv', 'w', encoding='utf-8', newline='') as csv_write:
        data = list(csv.reader(csv_read))
        data_out = unpack2table(group_by_id_name(data), id_name)
        writer = csv.DictWriter(csv_write, fieldnames=data_out[0].keys())
        writer.writeheader()
        writer.writerows(data_out)


text = '''01,Artist,Otis Taylor
01,Title,Ran So Hard the Sun Went Down
01,Time,3:52
02,Artist,Waylon Jennings
02,Title,Honky Tonk Heroes (Like Me)
02,Time,3:29'''

with open('data1.csv', 'w', encoding='utf-8') as file:
    file.write(text)

condense_csv('data1.csv', id_name='ID')

with open('condensed.csv', encoding='utf-8') as file:
    print(file.read().strip())

sys.exit(999)


def str2datetime(dt: str) -> datetime:
    return datetime.strptime(dt, '%d/%m/%Y %H:%M')


def datetime2str(dt: datetime) -> str:
    return dt.strftime('%d/%m/%Y %H:%M')


def filter_by_max_datetime(table: dict) -> list:
    return sorted([(email, *max(value, key=lambda x: x[1])) for email, value in table.items()])


def group_by_email(table: list) -> dict:
    table_out = dict()
    for row in table:
        table_out[row['email']] = table_out.get(row['email'], list())
        table_out[row['email']].append([row['username'], str2datetime(row['dtime'])])
    return table_out


with open('name_log.csv', 'r', encoding='utf-8') as csv_fin, \
        open('new_name_log.csv', 'w', encoding='utf-8', newline='') as csv_fout:
    data_in = csv.DictReader(csv_fin)
    fieldnames = data_in.fieldnames
    writer = csv.writer(csv_fout)
    writer.writerow(fieldnames)
    writer.writerows(
        list(map(lambda x: (x[1], x[0], datetime2str(x[2])), filter_by_max_datetime(group_by_email(list(data_in))))))

sys.exit(999)


def filter_by_age(table: list) -> list:
    return list(filter(lambda x: float(x['age']) < 18, table))


def filter_by_survived(table: list) -> list:
    return list(filter(lambda x: int(x['survived']) == 1, table))


def order_by_sex(table: list) -> list:
    return sorted(table, key=lambda x: x['sex'], reverse=True)


with open('titanic.csv', 'r', encoding='utf-8') as csv_f:
    data = csv.DictReader(csv_f, delimiter=';')
    sys.stdout.writelines(name['name'] + '\n' for name in order_by_sex(filter_by_survived(filter_by_age(list(data)))))

sys.exit(999)


def sorted_by_count(dt_dict: dict) -> list:
    return sorted(dt_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)


def group_by_district(dt_list: list) -> dict:
    group = dict()
    for dt in dt_list:
        district = dt['district']
        number_of_access_points = int(dt['number_of_access_points'])
        group[district] = group.get(district, 0) + number_of_access_points
    return group


with open('wifi.csv', 'r', encoding='utf-8') as csv_file:
    data = csv.DictReader(csv_file, delimiter=';')
    # print(*data)
    for district, number_of_access_points in sorted_by_count(group_by_district(list(data))):
        sys.stdout.writelines(f"{district}: {number_of_access_points}\n")

sys.exit(999)


def group_by_domain(dt_list: list) -> dict:
    group = dict()
    for dt in dt_list:
        domain = dt['email'].split('@')[1]
        group[domain] = group.get(domain, 0) + 1
    return group


def sorted_by_count(dt_dict: dict) -> list:
    return sorted(dt_dict.items(), key=lambda x: (x[1], x[0]))


with open('data.csv', 'r', encoding='utf-8') as csv_file_in, \
        open('domain_usage.csv', 'w', encoding='utf-8', newline='') as csv_file_out:
    data = csv.DictReader(csv_file_in)
    writer = csv.writer(csv_file_out, delimiter=';')
    writer.writerow(['domain', 'count'])
    writer.writerows(sorted_by_count(group_by_domain(list(data))))

sys.exit(999)


def csv_columns(filename: str) -> dict:
    with open(filename, 'r', encoding='utf-8') as csv_file:
        values = csv.DictReader(csv_file)
        column_names = values.fieldnames
        group = dict()
        for value in values:
            for column_name in column_names:
                group[column_name] = group.get(column_name, list())
                group[column_name].append(value[column_name])
        return group


def csv_columns2(filename):
    with open(filename, encoding="utf-8") as file_in:
        rows = list(csv.reader(file_in))
        return {key: value for key, *value in zip(*rows)}


# TEST_1:
text = '''movie,year,rating
Machete,2010,72
Marvin's Room,1996,80
Raging Bull,1980,97
This Boy's Life,1993,75
Silver Linings Playbook,2012,92
Taxi Driver,1976,99
Jackie Brown,1997,87
Shark Tale,2004,35
Bang the Drum Slowly,1973,88
Analyze That,2002,27
Meet the Parents,2000,84
Wag the Dog,1997,85
The Big Wedding,2013,7
Night and the City,1992,67
Backdraft,1991,71
The Untouchables,1987,80
Cop Land,1997,72
Thunderheart,1992,87
Being Flynn,2012,51
We're No Angels,1989,47
Limitless,2011,70
The Bag Man,2014,9
The Good Shepherd,2006,54
Jacknife,1989,64
Righteous Kill,2008,19
Mad Dog and Glory,1993,78
Brazil,1985,98
Mary Shelley's Frankenstein,1994,39
Stone,2010,50
Killer Elite,2011,25
A Bronx Tale,1993,96
Falling in Love,1984,60
The Adventures of Rocky & Bullwinkle,2000,43
Red Lights,2012,29
The Score,2001,73
New Year's Eve,2011,7
Ronin,1998,68
Midnight Run,1988,96
Last Vegas,2013,46
Born to Win,1971,40
Angel Heart,1987,78
City by the Sea,2002,48
Cape Fear,1991,76
Everybody's Fine,2009,46
Goodfellas,1990,96
15 Minutes,2001,33
Mistress,1991,69
Hide and Seek,2005,13
The Intern,2015,61
Awakenings,1990,88
Joy,2015,60
Mean Streets,1973,98
The Deer Hunter,1978,93
Great Expectations,1998,38
True Confessions,1981,75
The Mission,1986,65
Killing Season,2013,11
The King of Comedy,1983,90
New York,1977,67
Rent,2005,46
Once Upon a Time in America,1984,89
Meet the Fockers,2004,38
Bloody Mama,1970,17
The Last Tycoon,1976,41
Grudge Match,2013,29
Analyze This,1999,69
The Bridge of San Luis Rey,2005,4
Guilty by Suspicion,1991,65
What Just Happened?,2008,51
Heat,1995,86
Godsend,2003,4
Captain Shakespeare,2007,76
Flawless,1999,43
Stanley & Iris,1990,29
Arthur and the Invisibles,2007,21
Greetings,1968,86
Little Fockers,2010,10
Sleepers,1996,74
Dirty Grandpa,2016,11
Dear America: Letters Home From Vietnam,1987,100
Casino,1995,80
The Fan,1996,38
Heist,2015,26
Men of Honor,2000,41'''

with open('deniro.csv', 'w') as file:
    file.write(text)

start = time.perf_counter()
csv_columns('deniro.csv')
print(time.perf_counter() - start)
start = time.perf_counter()
csv_columns2('deniro.csv')
print(time.perf_counter() - start)

sys.exit(999)


def sorted_by_column_id(vals: list, col_id: int) -> list:
    data_types = {
        1: str,
        2: int,
        3: int
    }
    return sorted(vals, key=lambda x: data_types[col_id](x[col_id - 1]))


column_id = list(map(int, sys.stdin))[0]

with open('deniro.csv', 'r', encoding='utf-8') as csv_file:
    delimiter = ','
    values = list(csv.reader(csv_file, delimiter=delimiter, quotechar="'"))
    [print(delimiter.join(row)) for row in sorted_by_column_id(values, column_id)]

sys.exit(999)


def group_by_company_name(slrs: list) -> dict:
    group = dict()
    for slr in slrs:
        group[slr['company_name']] = group.get(slr['company_name'], list())
        group[slr['company_name']].append(int(slr['salary']))
    return group


def aggregate_salary(grp_slrs: dict) -> list:
    return [(key, sum(value) / len(value)) for key, value in grp_slrs.items()]


def sorted_by_avg_salary(slrs: list) -> list:
    return sorted(slrs, key=lambda x: (x[1], x[0]))


with open('salary_data.csv', 'r', encoding='utf-8') as csv_file:
    salaries = list(csv.DictReader(csv_file, delimiter=';'))
    avg_salaries_by_company = aggregate_salary(group_by_company_name(salaries))
    for key in sorted_by_avg_salary(avg_salaries_by_company):
        print(key)

sys.exit(999)

with open('sales.csv', 'r', encoding='utf-8') as csv_file:
    sales = csv.DictReader(csv_file, delimiter=';', quotechar="'")
    sales = filter(lambda x: int(x['old_price']) > int(x['new_price']), sales)
    [print(sale['name']) for sale in sales]

sys.exit(999)

with open('writing_test.csv', 'w', encoding='utf-8') as csv_file:
    # создаем writer объект и указываем названия столбцов
    writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])
    # записываем первую строку с названиями столбцов
    writer.writeheader()
    # записываем строку с данными
    writer.writerow({'first_col': 'value1', 'second_col': 'value2'})
