def f(a, b):
    if a > b:
        return 1000000000000
    if a == b:
        return 1
    return min(f(a + 1, b), f(a + 2, b), f(a * 2, b)) + 1

def r(a, b, c):
    if a > b:
        return 0
    if a == b and c == mn:
        return 1
    return r(a + 1, b, c + 1) + r(a + 2, b, c + 1) + r(a * 2, b, c + 1)

mn = f(1, 28) - 1
print(r(1, 28, 0))

