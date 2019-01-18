import math

# This is very very slow for larger numbers

def cloak(night):
    global a
    global b
    a = 0
    b = False
    while b == False:
        a = a + 1
        for w in range(1, night + 1):
            if a % w != 0:
                break
            elif w == night:
                b = True
                print(a)
                break
            else:
                continue
