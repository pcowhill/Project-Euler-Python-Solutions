import math

def digy():
    tally = 0
    for i in range(1,10000000):
        number = i
        while not (number in [1,89]):
            total = 0
            for a in str(number):
                total = total + int(a)**2
            number = total
        if number == 89:
            tally = tally + 1
        if i % 100000 == 0:
            print(i/100000)
    print(tally)
