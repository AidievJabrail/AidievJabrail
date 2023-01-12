def f(n):
    if n < 10:
        return n
    if n >= 10:
        return n % 10 + f(n // 10)
def g(n):
    if n < 10:
        return n
    if n >= 10:
        return g(f(n))
su = 0
for i in range(10, 100):
    su += g(i)
print(su)