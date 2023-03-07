s = open("C://Users//HP//Desktop//Информатика//24data//k7-m26.txt").readline()
#s = 'ABCDF'
al = ''.join(sorted('qwertyuioplkjhgfdasmnbvcxz'))
k = 0
imax = -1
for i in range(len(s) - 2):
    cnt = s[i:i + 3]
    if al.find(cnt[1]) < al.find(cnt[0]) and al.find(cnt[1]) < al.find(cnt[2]):
        k += 1
        imax = max(i, imax)

print(k, imax)