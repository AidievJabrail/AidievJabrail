from itertools import *

k = 0

for i in permutations('iivvvv'):
    s = ''.join(i)
    if 'vvvv' in s:
        k += 1
print(k)