k = 0
def f(n, a):
    global k
    if n > 100000000:
        return
    if a > 18:
        return 
    if a == 18:
        k += 1
    f(n * 3, a + 5)
    f(n * 3 + 1, a)
    f(n * 3 + 2, a)
f(1, 8)
f(2, 8)
print(k)