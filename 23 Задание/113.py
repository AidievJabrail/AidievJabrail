a = [0] * 300
for i in range(2, 228):
    mn = 100000000000
    if i - 1 >= 1:
        mn = min(a[i - 1], mn)
    if i - 5 >= 1:
        mn = min(a[i - 5], mn)
    if i % 3 == 0:
        mn = min(a[i // 3], mn)
    a[i] += mn + 1
print(a[227])