import os
import sys
from zipfile import ZipFile
from datetime import datetime
import json


def size(value: int):
    units = ['B', 'KB', 'MB', 'GB']
    count = 0
    while value >= 1024:
        count += 1
        value //= 1024
    return f"{value} {units[count]}"


with ZipFile('desktop.zip') as zp:
    info = zp.infolist()
    for i in info:
        path, file = os.path.split(i.filename)
        if i.is_dir():
            print(f"{'  '*(len(path.split('/'))-1)}{path.split('/')[~0]}")
        else:
            if path:
                print(f"{'  '*len(path.split('/'))}{file} {size(i.file_size)}")
            else:
                print(f"{file} {size(i.file_size)}")


sys.exit(999)


def is_correct_json(string: any) -> bool:
    try:
        json.loads(string.decode('utf-8'))
        return True
    except:
        return False


with ZipFile('data.zip') as zp:
    arsenal_team = []
    for name in zp.namelist():
        with zp.open(name) as f:
            json_in = f.read()
            if is_correct_json(json_in):
                football_teams = json.loads(json_in)
                if football_teams['team'] == 'Arsenal':
                    arsenal_team.append(f"{football_teams['first_name']} {football_teams['last_name']}")
    print(*sorted(arsenal_team), sep='\n')

sys.exit(999)

with ZipFile('workbook.zip') as zp:
    # print(len(list(filter(lambda x: not x.endswith('/'), zp.namelist()))))
    info = zp.infolist()
    # print(f"Объем исходных файлов: {sum(list(map(lambda x: x.file_size, info)))} байт(а)")
    # print(f"Объем сжатых файлов: {sum(list(map(lambda x: x.compress_size, info)))} байт(а)")
    # print(max(list(filter(lambda y: y.file_size != 0, info)), key=lambda x: x.compress_size / x.file_size * 100).filename.split('/')[~0])
    data_out = list(map(lambda x: (os.path.basename(x.filename), datetime(*x.date_time), x.file_size, x.compress_size),
                        filter(lambda x: x.file_size != 0, info)))
    for data in sorted(data_out):
        print(data[0])
        print(f"  Дата модификации файла: {data[1]}")
        print(f"  Объем исходного файла: {data[2]} байт(а)")
        print(f"  Объем сжатого файла: {data[3]} байт(а)")
        print()
    print(info[0].date_time, sep='\n')
    print(*sorted(list(map(os.path.basename, map(lambda y: y.filename,
                                                 list(filter(
                                                     lambda x: x.file_size != 0 and datetime(*x.date_time) > datetime(
                                                         2021, 11, 30, 14, 22, 00), info)))))),
          sep='\n')
