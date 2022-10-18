for i in range(100, 1000):
    s = str(i)
    sum1 = int(s[0]) + 6
    sum2 = int(s[1]) + 9
    sum3 = int(s[2]) + 4
    a = [sum1, sum2, sum3]
    a.sort()
    if str(a[2]) + str(a[1]) + str(a[0]) == '11108':
        print(i)
        brea