import sys
sys.setrecursionlimit(5000)

def f(n):
    if n > 10000:
        return n - 10000
    if 1 <= n <= 10000:
        return f(n + 1) + f(n + 2)
print(f(10))