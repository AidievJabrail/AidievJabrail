from itertools import *

k = 0
gl = 'ioe'
word = 'tixo'

for i in permutations('tixoreck', 4):
    s = ''.join(i)
    su = 0
    cnt = 0
    for j in range(len(s)):
        if s[j] in gl:
            su += 1
        if s[j] == word[j]:
            cnt += 1
    if su == 2 and cnt == 2:
        k += 1
print(k)
        

