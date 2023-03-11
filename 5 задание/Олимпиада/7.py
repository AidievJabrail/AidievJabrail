def po(n):
    global ma
    cnt = [[0] * n for i in range(n)]
    for j in range(n):
        for i in range(n):
            cnt[j][n - i - 1] = ma[i][j]
    ma = cnt

def pro(n):
    global ma
    cnt = [[0] * n for i in range(n)]
    for j in range(n):
        for i in range(n):
            cnt[n - j - 1][i] = ma[i][j]
    ma = cnt
    

def cout(n):
    global ma, im, jm
    for i in range(n):
        for j in range(n):
            if i == im and jm == j:
                print('*', end=' ')
            else:
                print(ma[i][j], end=' ')
        print()
    print()

def down():
    global ma, im, jm
    while ma[im + 1][jm] != 1:
        im += 1
        if im == n - 1:
            im, jm = -1, -1
            break

     


s = '*.*********........**.*.**.*.**.*....*.**.*.**.*.**.*.**.*.**.*....*.**.******.**........***********'
ma = [[0] * 10 for i in range(10)]
k = 0
n = 10
for i in range(10):
    for j in range(10):
        if s[k] == '*':
            ma[i][j] = 1
        else:
            ma[i][j] = 0
        k += 1
ans = 0
cnt = ma
for i in range(10):
    for j in range(10):
        ma = cnt
        if ma[i][j] == 0:
            im, jm = i, j
            
            for t in range(1, 20):
                if im == -1:
                    ans += 1
                    break
                down()
                if im == -1:
                    ans += 1
                    break
                if t % 4 != 0:
                    po(n)
                    im, jm = jm, n - im - 1
                else:
                    pro(n)
                    im, jm = n - jm - 1, im
print(ans)