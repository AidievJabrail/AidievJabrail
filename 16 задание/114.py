def is_pri(n):
    if n == 1 or n == 0:
        return 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            return 0
        i += 1
    return 1

def f(n):
    if n == 0:
        return 1
    if n > 0:
        return 7 * (n - 1) + f(n - 1)
sum = 0
for i in range(2, 201):
    if is_pri(f(i)):
        sum += 1
print(sum)