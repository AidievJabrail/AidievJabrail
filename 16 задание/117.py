import sys
k = 0
def f(n, a):
    global k
    if n > 500000000:
        return 
    if a > 3:
        return
    if a == 3:
        k += 1
    f(n * 2, a)
    if n % 2 == 0:
        f(n + 1, a + 1)
f(1, 2)
print(k)