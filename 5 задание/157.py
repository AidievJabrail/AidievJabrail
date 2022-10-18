for i in range(0, 256):
    s = bin(i)[2:]
    s = (8 - len(s)) * '0' + s
    s = s.replace('1', '.')
    s = s.replace('0', '1')
    s = s.replace('.', '0')
    if int(s, 2) - i == 113:
        print(i)