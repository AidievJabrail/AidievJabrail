for x in range(10):
    nt1 = int('1234' + str(x))
    n1 = nt1 + 5
    nt2 = int('12' + str(x) + '34')
    n2 = nt2 + 5
    if (n1 + n2) % 14 == 0:
        print(x, (n1 + n2) / 14)
