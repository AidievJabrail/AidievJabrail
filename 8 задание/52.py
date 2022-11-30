from itertools import product 

k = 0

for i in product('komar', repeat = 4):
    s = ''.join(i)
    if s.count('a') <= 3:
        k += 1
print(k)