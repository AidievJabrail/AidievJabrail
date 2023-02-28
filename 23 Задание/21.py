def f(a, b):
    if a > b: return 0
    if a == b: return 1
    return f(a + 1, b) + f(tr(a), b)
def tr(a):
    a = str(a)
    s = ''
    for i in a:
        if i != '9':
            s += str(int(i) + 1)
        else:
            s += i
    return int(s)

print(f(25, 51))