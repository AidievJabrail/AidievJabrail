s = ''
maxx = -1
for i in range(50):
    s += '6'
    cnt = s
    while '66' in cnt:
        cnt = cnt.replace('66', '1')
        cnt = cnt.replace('11', '2')
        cnt = cnt.replace('22', '6')
    if cnt == "21":
        maxx = max(maxx, s.count('6'))
print(maxx)