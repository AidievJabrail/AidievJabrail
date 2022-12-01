from itertools import *

k = 0

for i in product('qwertyuioplkjhgfdsazxcvbnm', repeat = 4):
    s = ''.join(i)
    if s[0] == s[3] and s[1] == s[2]:
        k += 1
print(k)