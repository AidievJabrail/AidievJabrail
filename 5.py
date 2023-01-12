sum = 0
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                for x5 in range(2):
                    f1 = ((x2 or not x1) and (x3 or not x2) and (x4 or not x3) and (x5 or not x4))
                    f2 =  ((x1 and x2 and x3) ^ (x3 and x4 and x5))
                    if f1 or f2:
                        sum += 1
print(sum)