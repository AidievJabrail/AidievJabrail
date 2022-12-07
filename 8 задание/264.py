from itertools import *

k = 0

for i in product('ГЕКЭ023', repeat = 4):
    k += 1
    s = ''.join(i)
    fl = 1
    for j in range(len(s) - 1):
        if s[j] == s[j + 1]:
            fl = 0
    if s[0].isdigit() and fl:
        print(s, k)
        break