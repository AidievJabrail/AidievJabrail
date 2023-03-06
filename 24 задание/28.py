s = open("C://Users//HP//Desktop//Информатика//24data//k7b-2.txt").readline()
#s = 'DBACDBFDBAC'
cnt = ''
o = 'DBAC'
i = 0
while cnt in s:
    cnt += o[i]
    i += 1
    if i == 4: 
        i = 0
print(len(cnt) - 1)