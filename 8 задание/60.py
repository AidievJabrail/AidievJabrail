from itertools import *

k = 0

for i in product('абвгэюя', repeat = 5):
    s = ''.join(i)
    if 'э' not in s[1:-1] and 'ю' not in s[1:-1] and 'я' not in s[1:-1] and (s[0] == 'э' or s[0] == 'ю' or s[0] == 'я') \
        and (s[-1] == 'э' or s[-1] == 'ю' or s[-1] == 'я'):
            k += 1
print(k)

    