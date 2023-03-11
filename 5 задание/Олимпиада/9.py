from itertools import *

def f(s):
    return (int(s[0]) or int(s[1]) and  int(s[2])) and (int(s[1]) or int(s[2])\
        and int(s[3])) and (int(s[2]) or int(s[3]) and int(s[0]))

k1 = 0
k2 = 0
for i in product('01', repeat=4):
    s = ''.join(i)
    if f(s) == 1:
        k1 += 1
    if f(s) == 0:
        k2 += 1
print(k1, k2)
ans = 0
for i in str(6 ** 6 * 10 ** 10):
    ans += int(i)
print(ans)
