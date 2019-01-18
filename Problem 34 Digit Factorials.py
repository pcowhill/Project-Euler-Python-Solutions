import math

def digitz():
    total = 0
    for i in range(10, 2540160):
        totz = 0
        for j in str(i):
            totz += math.factorial(eval(j))
        if totz == i:
            total += i
        if i % 25000 == 0:
            print(i/2500000)
    print(total)
