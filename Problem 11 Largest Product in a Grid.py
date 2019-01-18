import math

def jenkins():
    fin = open('p11.txt')
    total = []
    for line in fin:
        total = total + line.strip().split()
    highest = 1
    fin = open('p11.txt')
    for line in fin:
        keeper = line.strip().split()
        for i in range(17):
            if (int(keeper[i])*int(keeper[i+1])*int(keeper[i+2])*int(keeper[i+3])) > highest:
                highest = (int(keeper[i])*int(keeper[i+1])*int(keeper[i+2])*int(keeper[i+3]))
                a = keeper[i]
                b = keeper[i+1]
                c = keeper[i+2]
                d = keeper[i+3]
    print(highest)
    for i in range(340):
        if (int(total[i])*int(total[i+20])*int(total[i+40])*int(total[i+60])) > highest:
            highest = (int(total[i])*int(total[i+20])*int(total[i+40])*int(total[i+60]))
            a = total[i]
            b = total[i+20]
            c = total[i+40]
            d = total[i+60]
    print(highest)
    for i in range(337):
        if (int(total[i])*int(total[i+21])*int(total[i+42])*int(total[i+63])) > highest:
            highest = (int(total[i])*int(total[i+21])*int(total[i+42])*int(total[i+63]))
            a = total[i]
            b = total[i+21]
            c = total[i+42]
            d = total[i+63]
    print(highest)
    for i in range(3,340):
        if (int(total[i])*int(total[i+19])*int(total[i+38])*int(total[i+57])) > highest:
            highest = (int(total[i])*int(total[i+19])*int(total[i+38])*int(total[i+57]))
            a = total[i]
            b = total[i+19]
            c = total[i+38]
            d = total[i+57]
    print(highest)
    print(a, b, c, d)
    
