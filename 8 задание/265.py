from itertools import *

k = 0
dp = set()

for i in  permutations('sportloto'):
    s = ''.join(i)
    if s[0] != 'o' and s[-1] != 'o':
        dp.add(s)
print(len(dp))
