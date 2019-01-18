import math

def pearl(divisors):
    current = 0
    check = 0
    adder = 1
    track = 0
    highest = 0
    while check == 0:
        current = current + adder
        for i in range(1, int(math.sqrt(current))):
            if (current % i) == 0:
                track = track + 1
        if track*2 > highest:
            highest = track*2
            print(highest, current)
        if track*2 >= divisors:
            return current
        track = 0
        adder = adder + 1
        
