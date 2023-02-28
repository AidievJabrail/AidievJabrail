def f(a, b):
    if a > b: return 0
    if a == b: return 1
    return f(a + 1, b) + f(tr(a), b)
def tr(a):
    if str(a)[-2] != '9':
        a += 10
    return a
print(f(11, 27))