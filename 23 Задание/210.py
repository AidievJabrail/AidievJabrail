st = set()
def f(a):
    global cnt
    if a > 99:
        return
    if 10 <= a <= 99:
        st.add(a)
    for i in range(1, a + 1):
        f(int(str(i) + str(a - i)))
    for i in range(1, a + 1):
        if a % i == 0:
            f(int(str(i) + str(a // i)))

f(8)
print(len(st))
