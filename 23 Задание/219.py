from sys import *
from functools import *
setrecursionlimit(1000)

lru_cache(None)
def f(a, b, c):
    if a > b:
        return 0
    if a == b and c == 30:
        return 1
    if a == b and c != 30:
        return 0
    return f(a + 1, b, c + 1) + f(a * 2, b, c) + f(a * 3, b, c)


print(f(1, 9217, 0))
