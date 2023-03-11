def fint(a, c):
    ma = '0123456789ABCDEF'
    s = ''
    while a > 0:
        s += ma[a % c]
        a //= c
    s = s[::-1]
    if s == '':
        return '0'
    return s


def fman(a, c):
    ma = '0123456789ABCDEF'
    s = ''
    for i in range(30):
        a *= c
        s += ma[int(a)]
        a -= int(a)
    return s


def pr(a, c):
    if a - int(a) == 0:
        return fint(a, c)
    else:
        return fint(int(a), c) + '.' + fman(a - int(a), c)

print(pr(5.1, 2))