import math

def derek(jeter):
    global a
    global b
    global c
    global d
    a = int('9' * jeter)
    b = False
    c = [0]
    d = 0
    while b == False:
        for x in range(0, a):
            steve = a * (a - x)
            if str(steve) == str(steve)[::-1]:
                c.append(steve)
                d = (a - x)
                break
            else:
                continue
        c.sort()
        if c[-1] >= (a-1)**2:
            b = True
            print(c[-1])
            break
        elif a >= 1:
            a = a-1
            continue
        else:
            print('nope')
            break
