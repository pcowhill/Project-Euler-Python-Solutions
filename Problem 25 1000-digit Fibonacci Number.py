import math

def indexme(digi):
    fibpre = 1
    fibpost = 2
    holder = 0
    counter = 3
    limiter = 10**(digi-1)
    while fibpost < limiter:
        holder = fibpost
        fibpost += fibpre
        fibpre = holder
        counter += 1
    print('F(' + str(counter) + ') = ' + str(fibpost))
