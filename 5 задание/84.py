for i in range(1, 10000):
    s = bin(i)[2:]
    if s.count('1') % 2 == 0:
        s += '1'
    else:
        s += '0'
    s += str(s.count('1') % 2)
    if int(s, 2) > 31:
        print(int(s, 2))
        break