from pprint import pprint

f = n = int(input())  # размер матрицы
a = [[0] * n for i in range(n)]  # создание матрицы нужного размера, заполнена 0
count = 0  # количество заполненных ячеек
dcc = {1:(0, 0)}
for i in range(n):   # заполнение 1 строки
    count += 1
    dcc[count] = (0, i)
    a[0][i] = count
j = 0   # указываем последнюю заполненную ячейку
i = n-1
n -= 1  # устанавливаем размер 1 блока 1 витка
while len(a)**2 != count:  #условие выхода из цикла
    for k in range(n):  #движение вниз
        j += 1
        count += 1
        dcc[count] = (j, i)
        a[j][i] = count  # заполнение матрицы
    for k in range(n):  #движение влево
        i -= 1
        count += 1
        dcc[count] = (j, i)
        a[j][i] = count
    for k in range(n-1):  #движение вверх
        j -= 1
        count += 1
        dcc[count] = (j, i)
        a[j][i] = count
    for k in range(n-1): #движение вправо
        i += 1
        count += 1
        dcc[count] = (j, i)
        a[j][i] = count
    n -= 2


def sumOn(g):
    i = 0
    out = 0
    while i < len(g):
        out += g[i][i]
        i += 1
    return out

mini = 11e9
p = 0
for i in range(f * f + 1):
    c = a.copy()
    for j in range(1, f * f + 1):
        q = dcc[j]
        if (i + j) % (f ** 2 + 1):
            c[q[0]][q[1]] = (i + j) % (f ** 2 + 1)
        else:
            c[q[0]][q[1]] = i
    if sumOn(c) <= mini:
        mini = sumOn(c)
        p = i

print(mini, p)