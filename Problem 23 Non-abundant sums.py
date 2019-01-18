import math

def blake():
    S = []
    A = []
    O = 0
    L = []
    for n in range(1, 28123):
        for i in range(1, n):
            if n % i == 0:
                L.append(i)
        if sum(L) > n:
            A.append(n)
            for i in A:
                S.append(n+i)
        L = []
        if n not in S:
            O += n
    print(O)
            
