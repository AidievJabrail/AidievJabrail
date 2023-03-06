def f(a, b, c):
    s = c.copy() + [a]
    if a < b:
        return f(a + 1, b, s) + f(a * 2, b, s)
    if a == b and 10 in c:
        return 1
    return 0


print(f(1, 21, []))
