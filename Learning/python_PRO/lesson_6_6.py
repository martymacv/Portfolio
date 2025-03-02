import sys
from collections import OrderedDict

from datetime import datetime

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

primes = [i for i in range(1, 20) if is_prime(i)]
print(primes)

sys.exit()
def custom_sort(ordered_dict: OrderedDict, by_values: bool = False) -> None:
    for key in sorted(ordered_dict, key=lambda x: (x, ordered_dict[x])[by_values]):
        ordered_dict.move_to_end(key)


# INPUT DATA:

# TEST_1:
data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)

print(data)

# TEST_2:
data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)

print(*data.items())

# TEST_3:
data = OrderedDict(a=11, b=2, c=34, d=4, e=59, f=600, g=7)
custom_sort(data, by_values=False)

print(*data.items())

# TEST_4:
data = OrderedDict(aq=1, qb=2, rc=3, ed=4, we=5, wf=6, ag=7)
custom_sort(data, by_values=True)

print(*data.items())

# TEST_5:
data = OrderedDict(a=11, b=2, c=34, d=4, e=59, f=600, g=7)
custom_sort(data)

print(*data.items())

# TEST_6:
data = OrderedDict(a=99, b=22, c=44, d=33, e=11, f=77, g=66, h=99, i=88)
custom_sort(data, by_values=True)

print(*data.items())

# TEST_7:
data = OrderedDict(e=11, i=88, b=22, a=99, g=66, c=44, d=33, h=99, f=77)
custom_sort(data, by_values=False)

print(*data.items())

# TEST_8:
data = OrderedDict(e=11, b=22, a=99, g=66, c=44, d=33, h=99, f=77, i=88)
custom_sort(data)

print(*data.items())

# TEST_9:
data1 = OrderedDict(e=11, b=22, a=99, g=33, c=33, d=33, h=99, f=77, i=88, k=44)
custom_sort(data1, by_values=True)

print(*data1.items())

sys.exit(999)
def shuffle(order_dict: OrderedDict) -> OrderedDict:
    repack = OrderedDict()
    for first, second in zip(order_dict.items(), reversed(order_dict.items())):
        repack[first[0]] = first[1]
        repack[second[0]] = second[1]
    return repack


data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

print(shuffle(data))
