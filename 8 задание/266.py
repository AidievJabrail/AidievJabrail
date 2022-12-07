from itertools import *

k = 0

for i in product('дейнптья', repeat = 4):
    k += 1
    s = ''.join(i)
    s1 = set(s)
    if len(s1) == len(s) and 'е' not in s and 'я' not in s:
        print(k)
