def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n / 2) - 1
    if n > 0 and n % 2 == 1:
        return 1 + f(n - 1)
sum = 0
for i in range(1000):
    if f(i) == 0:
        sum += 1
print(sum)