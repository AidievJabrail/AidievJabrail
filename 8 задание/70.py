from itertools import *

k = 0

for i in product('abvg', repeat = 5):
    s = ''.join(i)
    if s.count('g') == 1:
        if s[-1] == 'g':
            k += 1
    elif 'g' not in s:
        k += 1
print(k)