import sys
sys.setrecursionlimit(6000)
from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 4 and n % 2 == 1:
        return 1
    if n > 3 and n % 2 == 0:
        return f(n - 1) + f(n - 2) + f(n - 3)
print(f(2008) - f(2006))