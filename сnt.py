from functools import *
minn = 1000000000000

@lru_cache(None)
def f(u, step, i):
    a, b = u
    if a + b >= 95 and step == 2:
        global minn
        minn = min(minn, i)
        return
    if step == 2:
        return 0
    f((a + 1, b), step + 1, i)
    f((a * 4, b), step + 1, i)
    f((a, b + 1), step + 1, i)
    f((a, b * 4), step + 1, i)
    
    

for i in range(1, 90):
    f((5, i), 1, i)
print(minn)