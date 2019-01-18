import math

def future(width, height):
    total = 0
    steps = width + height
    area = 2**steps
    for i in range(area):
        if bin(i)[2:].zfill(steps).count('1') == width:
            total = total + 1
        if (i % int(0.01*area)) == 0:
            print(str(int(i/area*100))+'%')
    print(total)

def smart(width, height):
    print(math.factorial(width+height)/math.factorial(width)/math.factorial(height))

#do the smart thing
