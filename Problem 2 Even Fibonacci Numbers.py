import math

def fabby(nomi):
    perpon = [1,2]
    while perpon[-1] + perpon[-2] < nomi:
        perpon.append(perpon[-1] + perpon[-2])
    laplap = []
    for w in range(0, len(perpon)):
        if perpon[w] % 2 == 0:
            laplap.append(perpon[w])
        else:
            continue
    print('This is the sum of the evens:', sum(laplap))
