for i1 in range(100):
    for i2 in range(100):
        for i3 in range(100):
            if i1 + i2 + i3 - 9 * (2 ** (i1) + 2 ** (i2) + 2 ** (i3)) == 333:
                print(i1, i2, i3)