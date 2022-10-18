for i in range (4, 1000):
    sum = str(i % 4) + str(i % 2) + str(i % 5)
    if sum == '313':
        print(i)
        break