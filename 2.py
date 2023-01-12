def toBASEint(num, base):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = abs(num)
    b = alpha[n % base] 
    while n >= base :
        n = n // base
        b += alpha[n % base] 
    return ('' if num >= 0 else '-') + b[::-1] 
    
def toBaseFrac(frac, base, n = 20) :
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = ''
    while n :
        frac *= base
        frac = round(frac,n)
        b += str(int(frac))
        frac -= int(frac)
        n -= 1
    return b
cnt = 0
for x in range(1, 512):
    Number = str(x / 2048)
    Basein = 10
    Baseout = 2
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if '.' in Number :
        num, frac = map(str,Number.split('.'))
        num = int(num,Basein)
        a = toBASEint(num,Baseout)
        b = 0
        k = Basein
        for i in frac :
            b += alpha.index(i) / k
            k *= Basein
        b = toBaseFrac(b, Baseout)
        ans = a+'.'+b
    else :
        ans = toBASEint(int(Number,Basein),Baseout)
    if '111111' in ans:
        cnt += 1
print(cnt)

