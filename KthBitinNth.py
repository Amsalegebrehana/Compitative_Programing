def invert(s1):
    ss = ""
    for i in range(len(s1)):
        if s1[i] == '0':
            ss += '1'
        else:
            ss +='0'
    print(ss)
invert("100")