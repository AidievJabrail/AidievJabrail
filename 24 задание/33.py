s = open("C://Users//HP//Desktop//Информатика//24data//k7c-1.txt").readline()
#s = 'DBACDBFDBAC'
k = 0
for i in range(len(s) - 2):
    cnt = 0
    if s[i] in 'BCD':
        if s[i + 1] in 'BDE' and s[i] != s[i + 1]:
            if s[i + 2] in 'BCE' and s[i + 1] != s[i + 2]:
                cnt = 1
    k += cnt
    
print(k)