for i in range (100, 1000):
    s = str(i)
    sum1 = int(s[0]) * int(s[1])
    sum2 = int(s[1]) * int(s[2])
    a = [sum1, sum2]
    a.sort()
    if str(a[1]) + str(a[0]) == '123':
        print(i)
        break