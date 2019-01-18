import math

def letsdothis():
    fin = open('p67.txt')
    linenum = 0     #number of total lines
    totalnum = 0    #number of total numbers
    linelist = []   #temporary list of numbers on any given line
    totallist = []  #list of all numbers in order
    for line in fin:
        linenum += 1
        linelist = line.strip().split()
        totalnum += len(linelist)
        totallist += linelist
    totallist.reverse()
    while linenum > 1:
        linelist = totallist[:linenum]
        del totallist[:linenum]
        linenum -= 1
        for i in range(linenum):
            if int(linelist[i]) > int(linelist[i+1]):
                totallist[i] = str(int(totallist[i]) + int(linelist[i]))
            else:
                totallist[i] = str(int(totallist[i]) + int(linelist[i+1]))
    print(int(totallist[0]))
