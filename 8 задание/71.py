from itertools import *

k = 0
j = 1
for i in product('eiknyc', repeat = 3):
    s = ''.join(i)
    if s[0] == 'k':
        print(j)
        break
    j += 1