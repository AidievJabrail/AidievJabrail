from itertools import *

k = 0
sogl = 'krblk'
gl = 'oai'

for i in permutations('korabli', 6):
    s = ''.join(i)
    if s[0] in sogl:
        fl = 1
        for j in range(len(s) - 1):
            if s[j] in sogl and s[j + 1] in sogl or s[j] in gl and s[j + 1] in gl:
                fl = 0
                break
        if fl:
            k += 1
print(k)