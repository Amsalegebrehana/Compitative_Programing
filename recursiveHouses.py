l=['e','y','x','r']

def santa(l):
    if len(l) == 1:
        h=l[0]
        print(h)
    else:
        mid = len(l)//2
        fh=l[:mid]
        sh=l[mid:]
        santa(fh)
        santa(sh)

santa(l)
        