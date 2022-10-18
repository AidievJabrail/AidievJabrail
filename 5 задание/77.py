for i in range (1000, 10000):
    s = str(i)
    sum1 = int(s[0]) + int(s[1])
    sum2 = int(s[2]) + int(s[3])
    a = [sum1, sum2]
    a.sort()
    if str(a[1]) + str(a[0]) == '1311':
        print(i)