import math

def properdivs(num):
    totalsum = 0
    for i in range(1,int(num/2+1)):
        if num % i == 0:
            totalsum += i
    return totalsum

def amicablesum(cap):
    fullsum = 0
    for i in range(2,cap):
        temp1 = properdivs(i)
        temp2 = properdivs(temp1)
        if i == temp2 and i != temp1:
            fullsum += i
    return fullsum
