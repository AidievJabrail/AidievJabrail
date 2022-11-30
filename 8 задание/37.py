from itertools import product

k  = 0
fl = 0

for  i in product('akru', repeat = 5):
    s = ''.join(i)
    if s == 'rukaa':
        fl = 1
    if fl:
        k += 1
    if s == 'ukara' in s:
        fl = 0
print(k, fl)