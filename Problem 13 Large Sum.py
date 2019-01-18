import math

def carl():
    fin = open('largesum.txt')
    total = 0
    for line in fin:
        num = float(line.strip())
        total = total + num
    print(str(total)[0] + str(total)[2:11])
    print(total)
