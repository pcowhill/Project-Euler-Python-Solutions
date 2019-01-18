import math

def paul(phil):
    guy = []
    for w in range(1, phil + 1):
        guy.append(w)
    dude = sum(guy)**2
    gal = []
    for w in range(0, phil):
        gal.append(guy[w]**2)
    bro = sum(gal)
    print('The sum of the squares is', bro)
    print('The square of the sums is', dude)
    print('The difference of the two is', abs(bro-dude))
