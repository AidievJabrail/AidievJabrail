def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n / 2)
    if n > 0 and n % 2 == 1:
        return f(n - 1) + 3
sum = 0
for i in range(1, 1001):
    if f(i) == 18:
        sum += 1
print(sum)