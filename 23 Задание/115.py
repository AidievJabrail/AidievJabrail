a = [0] * 300
for i in range(2, 112):
    mn = 100000000000
    if i - 1 >= 1:
        mn = min(a[i - 1], mn)
    if i - 5 >= 1:
        mn = min(a[i - 5], mn)
    if i % 3 == 0:
        mn = min(a[i // 3], mn)
    a[i] += mn + 1
mn = a[111]
def f(a, b, c):
    if a > b or c > 6:
        return 0
    if a == b and  c == 6:
        return 1
    return f(a + 1, b, c + 1) + f(a + 5, b, c + 1) + f(a * 3, b, c + 1)
print(f(1, 111, 0))




