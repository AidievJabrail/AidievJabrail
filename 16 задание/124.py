from functools import lru_cache
@lru_cache(None)
def f(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return g(n) + f(n - 1)
    if n > 2 and n % 2 == 1:
        return f(n - 2) - 2 * g(n + 1)

@lru_cache(None)
def g(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return f(n - 3) + f(n - 2)
    if n > 2 and n % 2 == 1:
        return f(n + 1) - g(n - 1)
print(g(120))