from itertools import product

k = 0
for i in product('kot', repeat = 5):
    s = ''.join(i)
    if s.count('o') == 2:
        k += 1
print(k)
