k = 0
def f(n, a):
    global k
    if n > 1000000000:
        return
    if a > 7:
        return
    if a == 7:
        k += 1
    f(n * 2, a + 1)
    f(n * 2 + 1, a)
f(1, 5)
print(k)