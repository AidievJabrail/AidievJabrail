from itertools import *

k = 0

for i in product('012345678', repeat = 5):
    s = ''.join(i)
    if s[0] != '0' and int(s[0]) % 2 == 0 and s[-1] != '8' and s[-1] != '1' and s.count('3') <= 1:
        k += 1
print(k)