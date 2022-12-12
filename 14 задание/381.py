for x in range(10):
    nt1 = 28
    nt2 = int('1' + str(x) + '324')
    n1 = int('1' + str(x) + '342', 28)
    n2 = 2 * nt2 + 7
    if (n1 - n2) % 25 == 0:
        print(x, (n1 - n2) / 25)