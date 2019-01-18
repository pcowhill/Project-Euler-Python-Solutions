import math

def scoring():
    fin = open('p22.txt')
    line = fin.readline()
    list1 = line.split(sep=',')
    list2 = []
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for a in list1:
        list2.append(a[1:-1])
    list2.sort()
    totalscore = 0
    scoretracker = 0
    for i in range(len(list2)):
        for j in list2[i]:
            for k in range(26):
                if j == letters[k]:
                    scoretracker += k+1
        totalscore += scoretracker*(i+1)
        scoretracker = 0
    return totalscore
