s = open("C://Users//HP//Desktop//Информатика//24data//k7-m21.txt").readline()
#s = 'ABCDF'
k = 0
imax = -1
for i in range(len(s) - 2):
    cnt = s[i:i + 3]
    if list(cnt) == sorted(set(cnt)):
        k += 1
        imax = max(imax, i)

print(k, imax)