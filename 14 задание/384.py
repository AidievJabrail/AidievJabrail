for x in range(10):
    nt1 = int('132' + str(x) + '4')
    nt2 = 22
    n1 = nt1 + 3
    n2 = int('13' + str(x) + '42', nt2)
    if abs(n1 - n2) % 100 == 53:
        print(x, abs(n1 - n2) / 100)