from itertools import product

k = 0

for i in product("крот", repeat = 6):
    s = ''.join(i)
    if s.count('о') == 1:
        k += 1
print(k)