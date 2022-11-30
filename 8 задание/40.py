from itertools import product

k = 0

for i in product('abcdx', repeat = 4):
    s = ''.join(i)
    if s.count('x') == 1:
        k += 1
print(k)