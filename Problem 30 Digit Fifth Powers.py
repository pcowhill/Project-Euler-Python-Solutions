import math

def powersum(upper_bound):
    totalsum = 0
    for i in range(2, upper_bound):
        place = str(i)
        cold = 0
        for j in place:
            kool = int(j)
            cold += kool**5
        if cold == i:
            print(i)
            totalsum+=i
    print(totalsum)
