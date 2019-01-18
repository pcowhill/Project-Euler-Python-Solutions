import math

# I'm not sure why this doesn't work

def coinz():
    x = 8
    for a in range(0, 200):
        for b in range(0, 100):
            for c in range(0, 40):
                for d in range(0, 20):
                    for e in range(0, 10):
                        for f in range(0, 4):
                            for g in range(0, 2):
                                if 2 == (a*.01 + b*.02 + c*.05 + d*.1 + e*.2 + f*.5 + g):
                                    x += 1
        print(a/200, x)
    print('Done:', x)


def coinz2():
    coins = [1,2,5,10,20,50,100,200]
    target = 200
    ways = [1] + [0]*target

    for coin in coins:
        for i in range(coin, target+1):
            ways[i] += ways[i-coin]
    print(ways[target])
    
    
