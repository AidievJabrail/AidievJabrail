s = 'ab' * 52
while 'aa' in s or 'bb' in s or 'ab' in s:
    s = s.replace('aa', 'b', 1)
    s = s.replace('bb', 'a', 1)
    s = s.replace('ab', 'ba', 1)
print(s)