from itertools import product

sum = 0
numbers = product("АОУ", repeat = 5)
for i in numbers:
    sum += 1
    if sum == 101:
        print(''.join(i))