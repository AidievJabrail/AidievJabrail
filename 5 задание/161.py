for i in range(1, 101):
    s = bin(i)[2:]
    s = s[::-1]
    if int(s, 2) == 7:
        print(i)