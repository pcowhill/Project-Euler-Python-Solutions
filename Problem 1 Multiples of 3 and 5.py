import math

def eminem(stan):
    dido = [0]
    for x in range(0, stan):
        if x % 5 == 0:
            dido.append(x)
        elif x % 3 == 0:
            dido.append(x)
        else:
            continue
    print(dido)
    print(sum(dido))
    
