for i in range(1000, 10000):
    s = str(i)
    sum1 = int(s[0]) + int(s[2]) 
    sum2 = int(s[1]) + int(s[3])
    sum1, sum2 = max(sum1, sum2), min(sum1, sum2)
    if str(sum2) + str(sum1) == '35':
        print(i)
