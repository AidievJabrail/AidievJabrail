from functools import lru_cache
@lru_cache(None)
def f(n):
    if n <= 3:
        return n + 3
    f1 = f(n - 1)
    f2 = f(n - 2)
    if n > 3 and f1 % 2 == 0:
        return f2 + n
    if n > 3 and f1 % 2 == 1:
        return f2 + 2 * n
su = 0
for i in range(40, 51):
    su += f(i)
print(su)