from itertools import *

def boo(a, s):
    for i in range(len(a)):
        if a[i] == s[i]:
            return 0
    return 1
a = input()
fl = 0

for i in permutations(a):
    s = ''.join(i)
    if fl == 0 and boo(s, a):
        fir = s
        fl += 1
    if fl == 1 and boo(s, a) and boo(s, fir):
        sec = s
        fl += 1
    if fl == 2:
        break
if fl == 2:
    print(fir)
    print(sec)
else:
    print("IMPOSSIBLE")
