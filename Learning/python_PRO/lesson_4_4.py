import csv
import json
import sys
from datetime import datetime, time


# Напишите программу, которая определяет все виды заведений и для каждого вида находит
# самое большое заведение этого вида (имеет наибольшее количество посадочных мест).
# Программа должна вывести все виды заведений в лексикографическом порядке,
# указав для каждого самое большое заведение и количество посадочных мест в нем.
# Данные о заведениях должны быть расположены каждые на отдельной строке, в следующем формате:
# <вид заведения>: <название заведения>, <количество посадочных мест>

def group_by_type_object(table: list) -> list:
    type_objects = dict()
    for row in table:
        type_objects[row['TypeObject']] = type_objects.get(row['TypeObject'], list())
        type_objects[row['TypeObject']].append((row['Name'], row['SeatsCount']))
    for type_object, name in type_objects.items():
        type_objects[type_object] = max(name, key=lambda x: x[1])
    return sorted(map(lambda x: (x[0], *x[1]), type_objects.items()))

# def group_by_operating_company(table: list) -> str:
#     operating_companies = dict()
#     for row in table:
#         operating_companies[row['OperatingCompany']] = operating_companies.get(row['OperatingCompany'], 0) + 1
#     del operating_companies['']
#     operating_company, quantity = max(operating_companies.items(), key=lambda x: x[1])
#     return f"{operating_company}: {quantity}"


with open('food_services.json', encoding='utf-8') as json_in:
    data = json.load(json_in)
    for type_object, name, seats_count in group_by_type_object(data):
        print(f"{type_object}: {name}, {seats_count}")


sys.exit(999)
def str2datetime(dtm: str) -> datetime:
    return datetime.strptime(dtm, '%Y-%m-%d %H:%M:%S')


def sorted_by_score(table_data: list) -> list:
    return sorted(table_data,
                  key=lambda x: (x['name'], x['surname'], x['score'], str2datetime(x['date_and_time'])),
                  reverse=True)


def filter_by_max_score(table_data: list) -> list:
    table_out = [table_data[0]]
    for i in range(1, len(table_data)):
        if table_data[i - 1]['name'] != table_data[i]['name'] \
                or table_data[i - 1]['surname'] != table_data[i]['surname']:
            table_out.append(table_data[i])
    return table_out


def sorted_by_email(table_data: list) -> list:
    return sorted(table_data, key=lambda x: x['email'])


def rename_column(table_data: list) -> list:
    table_out = table_data
    for row in table_out:
        row.update({'best_score': row.pop('score')})
        row['best_score'] = int(row.pop('best_score'))
        row.update({'date_and_time': row.pop('date_and_time')})
        row.update({'email': row.pop('email')})
    return table_out


with (open('exam_results.csv', encoding='utf-8') as csv_in,
      open('best_scores.json', 'w', encoding='utf-8') as json_out):
    reader = list(csv.DictReader(csv_in))
    data = sorted_by_email(filter_by_max_score(sorted_by_score(reader)))
    json.dump(rename_column(data), json_out, indent=3)



"""sys.exit(999)

def str2time(tms: str) -> list:
    return list(map(lambda x: datetime.strptime(x, '%H:%M').time(), tms.split('-')))


def filter_by_times(tms: list) -> bool:
    return tms[0] <= time(hour=10, minute=00) <= time(hour=12, minute=00) <= tms[1]


def times_to_swim(pools: list):
    return list(filter(lambda x: filter_by_times(str2time(x['WorkingHoursSummer']['Понедельник'])), pools))


def filter_max_length(pools: list) -> list:
    max_length = max(pools, key=lambda x: x['DimensionsSummer']['Length'])['DimensionsSummer']['Length']
    return list(filter(lambda x: x['DimensionsSummer']['Length'] == max_length, pools))


def filter_max_width(pools: list) -> list:
    max_width = max(pools, key=lambda x: x['DimensionsSummer']['Width'])['DimensionsSummer']['Width']
    return list(filter(lambda x: x['DimensionsSummer']['Width'] == max_width, pools))


with open('pools.json', encoding='utf-8') as json_in:
    data_in = json.load(json_in)
    data_out = filter_max_width(filter_max_length(times_to_swim(data_in)))[0]
    print(f"{data_out['DimensionsSummer']['Length']}x{data_out['DimensionsSummer']['Width']}")
    print(f"{data_out['Address']}")


sys.exit(999)
with (open('students.json', encoding='utf-8') as json_in,
      open('data.csv', 'w', encoding='utf-8', newline='') as csv_out):
    data_in = filter(lambda x: x['age'] >= 18 and x['progress'] >= 75, json.load(json_in))
    data_out = [dict(filter(lambda x: x[0] in ('name', 'phone'), row.items())) for row in data_in]
    writer = csv.DictWriter(csv_out, fieldnames=data_out[0].keys())
    writer.writeheader()
    writer.writerows(sorted(data_out, key=lambda x: list(x.items())[0]))


sys.exit(999)
with (open('playgrounds.csv', encoding='utf-8') as csv_in,
      open('addresses.json', 'w', encoding='utf-8') as json_out):
    data_csv = csv.DictReader(csv_in, delimiter=';')
    # print(*data_csv)
    data_in = list(data_csv)
    data_out = dict()
    print(data_in)
    for row in data_in:
        data_out[row['AdmArea']] = data_out.get(row['AdmArea'], dict())
        data_out[row['AdmArea']][row['District']] = data_out[row['AdmArea']].get(row['District'], list())
        data_out[row['AdmArea']][row['District']].append(row['Address'])
    json.dump(data_out, json_out, indent=3, ensure_ascii=False)

sys.exit(999)

with (open('countries.json', encoding='utf-8') as json_in,
      open('religion.json', 'w', encoding='utf-8') as json_out):
    data_in = json.load(json_in)
    data_out = dict()
    for country in data_in:
        data_out[country['religion']] = data_out.get(country['religion'], list())
        data_out[country['religion']].append(country['country'])
    json.dump(data_out, json_out, indent=3)


sys.exit(999)

with (open('people.json', encoding='utf-8') as json_in,
      open('updated_people.json', 'w', encoding='utf-8') as json_out):
    data_in = json.load(json_in)
    keys = set()
    for key in map(lambda x: set(x.keys()), data_in):
        keys.update(key)
    for elem in data_in:
        for key in keys:
            elem[key] = elem.get(key, None)
    json.dump(data_in, json_out, indent=3)


sys.exit(999)

with (open('data1.json', encoding='utf-8') as json_in1,
      open('data2.json', encoding='utf-8') as json_in2,
      open('data_merge.json', 'w', encoding='utf-8') as json_out):
    data1: dict = json.load(json_in1)
    data1.update(json.load(json_in2))
    json.dump(data1, json_out, indent=3)



with open('data.json', encoding='utf-8') as json_in, \
        open('updated_data.json', 'w', encoding='utf-8') as json_out:
    data_in = list(filter(lambda x: x is not None, json.load(json_in)))
    for i in range(len(data_in)):
        if isinstance(data_in[i], str):
            data_in[i] += '!'
        elif isinstance(data_in[i], bool):
            data_in[i] = (True, False)[data_in[i]]
        elif isinstance(data_in[i], (int, float)):
            data_in[i] += 1
        elif isinstance(data_in[i], list):
            data_in[i] += data_in[i]
        elif isinstance(data_in[i], dict):
            data_in[i]["newkey"] = None
    json.dump(data_in, json_out, indent=3)

sys.exit(999)
string = sys.stdin.read()

for key, value in json.loads(string).items():
    print(f"{key}:", end=' ')
    if type(value) is not list:
        print(value)
    else:
        print(', '.join(map(str, value)))

# INPUT DATA:

# TEST_1:
{"size": 36, "style": "bold", "name": "text1", "alignment": "center"}

# TEST_2:
{
    "type": "donut",
    "name": "Cake",
    "tastes": ["chocolate", "cream", "strawberry"]
}

# TEST_3:
{
    "type": ["chocolate", "cream", "strawberry"],
    "name": ["chocolate", "cream", "strawberry"],
    "tastes": ["chocolate", "cream", "strawberry"]
}

# TEST_4:
{
    "type": "chocolate",
    "name": "chocolate",
    "tastes": "chocolate"
}

# TEST_5:
{"src": "Images/Sun.png",
 "name": "sun1",
 "hOffset": 250,
 "vOffset": 250,
 "alignment": "center"}

# TEST_6:
{
    "src": "Images/Sun.png",
    "name": "sun1",
    "hOffset": 250,
    "AAA": ["ABC", 123, 123, "XYZ"],
    "vOffset": 250,
    "alignment": "center",
    "key": [1, 2, 3, 4, 5],
    "another_key": ["a", "b", "c"]
}

# TEST_7:
{
    "another_key1": ["a", "b", "c"],
    "AAA": ["ABC", 123, 123, "XYZ"],
    "another_key2": ["a", "b", "c", "g"],
    "another_key3": ["a", "b", "c", 10],
    "another_key4": [9, 8, "pog", "a", "b", "c"],
    "key": [1, 2, 3, 4, 5],
    "another_key5": ["a", "b", "c"]
}

# TEST_8:
{"another_key1": "b",
 "AAA": "ABC",
 "another_key2": "g",
 "another_key3": 0,
 "another_key4": "pog",
 "key": "[1, 2, 3, 4, 5]",
 "another_key5": "c"}

# TEST_9:
{"another_key1": "b",
 "AAA": "ABC",
 "another_key2": "g",
 "anoth756er_key3": 0,
 "anothe645r_key5": "cdfg",
 "anoth645er_key5": "fhc",
 "anothe53r_key5": "cfgh",
 "another_key5": "chfg",
 "another_k234ey5": "gfc",
 "anothe123r_key5": "sdfc",
 "anotqwefdsher_key5": "cfsd"}

# TEST_10:
{
    "another_key1": 1,
    "AAA": 2,
    "another_key2": 3
}

sys.exit(999)
specs = {
    'Модель': 'AMD Ryzen 5 5600G',
    'Год релиза': 2021,
    'Сокет': 'AM4',
    'Техпроцесс': '7 нм',
    'Ядро': 'Cezanne',
    'Объем кэша L2': '3 МБ',
    'Объем кэша L3': '16 МБ',
    'Базовая частота': '3900 МГц'
}

specs_json = json.dumps(specs, ensure_ascii=False, indent=3)

print(specs_json)

club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
         "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}

club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
         "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}

club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
         "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}

with open('data.json', 'w') as json_f:
    json.dump([club1, club2, club3], json_f, indent=3)

countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
             'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
             'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
             'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

print(json.dumps(countries, indent=3, separators=(',', ' - '), sort_keys=True))

words = {
    frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
    "travel": "trævl",
    ("hello", "world"): ("həˈləʊ", "wɜːld"),
    "moonlight": "muːn.laɪt",
    "sunshine": "ˈsʌn.ʃaɪn",
    ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
    "adventure": "ədˈventʃər",
    "beautiful": "ˈbjuːtɪfl",
    frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
    "bicycle": "baisikl",
    ("pilot", "fly"): ("pailət", "flai")
}

data_json = json.dumps(words, skipkeys=True)
print(data_json)
"""