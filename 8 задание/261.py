from itertools import *

k = 0
sum = 0

for i in product("aejimy", repeat = 5):
    k += 1
    s = ''.join(i)
    fl = 1
    for j in range(len(s) - 1):
        if s[j] == s[j + 1]:
            fl = 0
            break
    if fl and k % 2 == 0:
        sum += 1
print(sum)