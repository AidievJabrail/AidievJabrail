from functools import lru_cache
def par(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    if sum % 2 == 0:
        return 1
    else:
        return 0
@lru_cache(None)
def f(n):
    if n < 3:
        return 1
    if n > 2 and par(n):
        return f(n - 1) - f(n - 2)
    if n > 2 and par(n) == 0:
        return f(n - 1) + f(n // 2)
print(f(100))