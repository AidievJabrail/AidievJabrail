from itertools import *

k = 0
gl = 'аиуоия'
def bo(s1, s2):
    le = 0
    ri = 0
    for i in s1:
        if i in gl:
            le += 1
    for j in s2:
        if j in gl:
            ri += 1
    return abs(ri - le) == 1

st = set()

for i in range(0, 7):
    for j in product('антиутопия', repeat = i):
        s1 = ''.join(j)
        for z in product('антиутопия', repeat = 6 - i):
            s2 = ''.join(z)
            if bo(s1, s2):
                st.add(s1 + s2)
                k += 1
print(len(st), k)

