import cmath
import math
from datetime import datetime
import sys


dates = list(map(int, sys.stdin))

print(f'Рост самого низкого ученика: {min(dates)}')
print(f'Рост самого высокого ученика: {max(dates)}')
print(f'Средний рост: {sum(dates)/len(dates)}')