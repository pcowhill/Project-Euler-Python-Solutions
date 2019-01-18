import math

def scorez():
    f = open('p042_words.txt','r')
    line = f.readline()
    prewords = line.split(sep=',')
    words = []
    for i in prewords:
        words.append(eval(i))
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    scoretracker = 0
    total = 0
    trianglenumbers = []
    for n in range(50):
        trianglenumbers.append(.5*n*(n+1))
    for i in words:
        for j in i:
            for k in range(26):
                if j == letters[k]:
                    scoretracker += k+1
        if scoretracker in trianglenumbers:
            total += 1
        scoretracker = 0
    return total
