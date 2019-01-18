import math

def spiraly(side):
    area = side**2 + 1
    numbers = []
    for i in range(1,area):
        numbers.append(i)
    skipper = 2
    tracker = 0
    totalsum = 0
    while len(numbers) > 0:
        if tracker == 4:
            tracker = 0
            skipper += 2
        else:
            totalsum += numbers[0]
            del numbers[:skipper]
            tracker += 1
    return totalsum
