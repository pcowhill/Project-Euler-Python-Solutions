import math

def protection(nester):
    a = 2**nester
    b = str(a)
    c = []
    for w in range(0, len(b)):
        c.append(eval(b[w]))
    print(sum(c))
    
