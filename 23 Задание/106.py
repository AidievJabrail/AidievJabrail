def f(a, b, c):
    if a > b:
        return 0
    if a == b and c == 8:
        return 1
    return f(a + 1, b, c + 1) + f(a * 2, b, c + 1) + f(a * 3, b, c + 1)
print(f(1, 34, 0))