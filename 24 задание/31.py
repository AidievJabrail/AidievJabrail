s = open("C://Users//HP//Desktop//Информатика//24data//k7b-5.txt").readline()
#s = 'DBACDBFDBAC'
cnt = ''
o = 'CA'
i = 0
while cnt in s:
    cnt += o[i]
    i += 1
    if i == 2: 
        i = 0
print(len(cnt) - 1)