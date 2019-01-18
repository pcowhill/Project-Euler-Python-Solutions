import math

def tryhard(broth):
    a = 1
    b = 1
    c = 1
    z = False
    while z == False:
        if a == 999:
            a = 1
            b = b + 1
            continue
        elif a + b + math.sqrt(a**2 + b**2) == broth:
            c = math.sqrt(a**2 + b**2)
            print(a, '*', b, '*', c, '=', a*b*c)
            z = True
            break
        else:
            a = a+1
            continue
