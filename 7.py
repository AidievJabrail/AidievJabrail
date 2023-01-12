s = 'abccba'
while 1:
    s = s.replace('cc', 'bcacb')
    if len(s) == 80808501:
        print(s)
        break
    s = s.replace('bb', 'acbca')
    if len(s) == 80808501:
        print(s)
        break
    s = s.replace('aa', 'cbabc')
    if len(s) == 80808501:
        print(s)
        break
    if len(s) > 80808501:
        break