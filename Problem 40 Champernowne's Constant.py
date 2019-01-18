import math

def constantz():
    a = ''
    i = 0
    while len(a) < 1000001:
        a += str(i)
        i += 1
    print(float(a[1])*float(a[10])*float(a[100])*float(a[1000])*float(a[10000])*float(a[100000])*float(a[1000000]))
