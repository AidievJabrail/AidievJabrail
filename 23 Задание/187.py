def f(a, b, c):
    if a == b and c.count('3') < 3:
        return 1
    if a < b:
        ans = f(a + 2, b, c + '1') + f(a + 3, b, c + '2')
        if a % 2 == 1:
            ans += f(a * 2, b, c + '3')
        return ans
    return 0


print(f(3, 46, ''))
