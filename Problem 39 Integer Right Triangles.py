import math

def irt():
    toptally = -1
    topp = -1
    for p in range(1,1001):
        tally = 0
        for i in range(1,int(p/2)):
            for j in range(1, i):
                h = math.sqrt(i**2+j**2)
                if h == int(h):
                    if h + i + j == p:
                        tally = tally + 1
        if tally > toptally:
            toptally = tally
            topp = p
        print(p)
    print(topp, toptally)
