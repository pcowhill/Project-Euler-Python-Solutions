import math

def pali(x):
    top = x
    sum = 0
    for i in range(1,top):
        if str(i) == str(i)[::-1]:
            if str(bin(i)[2:]) == str(bin(i)[2:])[::-1]:
                sum += i
    print(sum)
    
