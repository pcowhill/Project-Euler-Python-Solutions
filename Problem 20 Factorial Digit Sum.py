import math

def summy(num):
    factorial = math.factorial(num)
    summer = 0
    for i in str(factorial):
        summer = summer + int(i)
    return summer
