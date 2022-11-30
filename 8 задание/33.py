from itertools import permutations, product

k = 0

fl = 0  
for i in product('oprt', repeat = 5):
    s = ''.join(i)
    if s == 'ropot':
        fl = 1
    if fl == 1:
        k += 1
    if s == 'topor':
        fl = 0
print(k)