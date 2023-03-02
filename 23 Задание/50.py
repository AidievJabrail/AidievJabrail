def f(a, b, c):
    if a > b: return 0
    if a == b and c[-2] == '1': return 1
    return f(a + 1, b, c + '1') + f(a * 2, b, c + '2')
print(f(5, 32, ''))
