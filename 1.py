n = 15 ** 14
ans = ((n * (n + 1)) // 2) ** 2
s = str(ans)
sum = 0
for i in s:
    sum += int(i)
print(sum)