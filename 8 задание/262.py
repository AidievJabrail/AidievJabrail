from itertools import *

k = 0

for i in product('01234567', repeat = 5):
    s = ''.join(i)
    if (s.count('6') == 1 and '67' not in s and '65' not in s and '63' not in s and '61' not in s 
    and '76' not in s and '56' not in s and '36' not in s and '16' not in s and s[0] != '0'):
        k += 1
print(k)
    