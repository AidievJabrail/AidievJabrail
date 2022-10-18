for i in range(1, 10000):
    s = bin(i)[2:]
    if i % 2 == 0:
        s += '01'
    else:
        s += '10'
    if int(s, 2) > 62:
        print(int(s, 2))
        break