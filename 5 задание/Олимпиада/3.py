Path='RRRL'
ans=0
for x in range(10):
    for y in range(10):
        A=[]
        A.append(list("*.********"))
        A.append(list("*........*"))
        A.append(list("*.*.**.*.*"))
        A.append(list("*.*....*.*"))
        A.append(list("*.*.**.*.*"))
        A.append(list("*.*.**.*.*"))
        A.append(list("*.*....*.*"))
        A.append(list("*.******.*"))
        A.append(list("*........*"))
        A.append(list("**********"))
        if A[x][y]!='*':
            C=[x,y]
            A[C[0]][C[1]]='O'
            while A[C[0]+1][C[1]]!='*':
                C[0]+=1
                A[C[0]][C[1]]='o'
            D=0 #Направление: 0 - вниз, 1 - вправо, 2 - вверх, 3 - влево
            out=False
            for i in range(len(Path)):
                if not out:
                    D=(D+1)%4 if Path[i]=='R' else (D+3)%4
                    if D==0:
                        while A[C[0]+1][C[1]]!='*':
                            C[0]+=1
                            A[C[0]][C[1]]='o'
                    elif D==1:
                        while A[C[0]][C[1]+1]!='*':
                            C[1]+=1
                            A[C[0]][C[1]]='o'
                    elif D==2:
                        while A[C[0]-1][C[1]]!='*':
                            C[0]-=1
                            A[C[0]][C[1]]='o'
                            if C==[0,1]:
                                print('Finish from', x, y)
                                for i in A:
                                    print("".join(i))
                                out=True
                                ans+=1
                                break
                    else:
                        while A[C[0]][C[1]-1]!='*':
                            C[1]-=1
                            A[C[0]][C[1]]='o'
print(ans)
