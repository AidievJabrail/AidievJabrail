from itertools import product

k = 0
for i in product("лето", repeat = 4):
    if i[0] == 'л' or i[0] == 'т':
        k += 1
print(k)