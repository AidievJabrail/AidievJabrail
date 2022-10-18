for i in range(100, 1000):
    s = str(i)
    sum1 = int(s[0]) + int(s[1]) 
    sum2 = int(s[1]) + int(s[2])
    sum1, sum2 = max(sum1, sum2), min(sum1, sum2)
    if str(sum1) + str(sum2) == '157':
        print(i)
        break
