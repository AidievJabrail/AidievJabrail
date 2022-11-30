from itertools import product

k = 0

for i in product('pirog', repeat = 5):
    s = ''.join(i)
    if s.count('r') == 2 and (s.count('ro') == 2 or s.count('ri') == 2 \
        or (s.count('ro') == 1 and s.count('ri') == 1)):
        k += 1
    if s.count('r') == 1 and (s.count('ro') == 1 or s.count('ri') == 1):
        k += 1
    if s.count('r') == 0:
        k += 1
print(k)