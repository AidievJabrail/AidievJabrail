def f(a, b, c):
    s = c.copy() + [a]
    if a < b:
        return f(a + 1, b, s) + f(a * 2, b, s)
    if a == b and 20 in c and 12 not in c:
        return 1
    return 0


print(f(3, 30, []))
