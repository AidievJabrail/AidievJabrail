amin = 1000000000000
k = 0
ma = []
for i in open("C://Users//User//Desktop//24data (8)//24-s1.txt"):
    ma.append(i)
    if amin > i.count('A'):
        amin = i.count('A')
        ib = k
    k += 1
d = dict()
for i in ma[ib]:
    if i in d:
        d[i] += 1
    else:
        d[i] = 0
d = dict(sorted(d.items()))
mx = -1
for i in d:
    if mx <= d[i]:
        ans = i
        mx = d[i]
ma = ''.join(ma)
print(ans, ma.count(ans))
