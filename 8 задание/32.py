from itertools import product

k = 0

for i in product('abcd', repeat = 3):
    s = ' '
    s += ''.join(i)
    s += ' '
    if 'bc' not in s and 'cb' not in s:
        for j in range(1, len(s) - 1):
            if s[j] == 'a':
                if s[j + 1] != 'd' and s[j - 1] != 'd':
                    k -= 1
                    break
        k += 1
                    
print(k)