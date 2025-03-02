import csv
import sys
from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
min_values = lambda: list(filter(lambda y: y[1] == min(data.items(), key=lambda x: x[1])[1], list(data.items())))
max_values = lambda: list(filter(lambda y: y[1] == max(data.items(), key=lambda x: x[1])[1], list(data.items())))
data.__dict__.update({'min_values': min_values})
data.__dict__.update({'max_values': max_values})

print(data.min_values())
print(data.max_values())

sys.exit()

str_input = """Тимур 100
Анри 88
Дима 94
Артур 82
Владимир 90"""

rare_word_list = defaultdict(list)
for key, value in Counter(str_input.split()).items():
    rare_word_list[value].append(key)
print(max(rare_word_list[max(rare_word_list.keys(), key=lambda x: x)], key=lambda x: x))

for ln, cnt in sorted(Counter(len(word) for word in str_input.split()).most_common(), key=lambda x: x[1]):
    print(f"Слов длины {ln}: {cnt}")

print(Counter(len(word) for word in str_input.split()).most_common())

counter = Counter()
for line in str_input.splitlines():
    key, value = line.split()
    counter.update(Counter({key: int(value)}))

print(counter.most_common()[~1][0])
