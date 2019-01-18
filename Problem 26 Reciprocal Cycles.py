import math

# put n and m as the range you'd like to survey and the result
#   will be a print of d (in 1/d) and 1/d represented in
#   decimal notation where 0.6(6) means 0.66666...

def jack(n, m):
    f = '0'
    g = 0
    for i in range(n, m):
        x = '0.'+'0'*(len(str(i))-1)
        a = 10**(len(str(i)))
        b = math.floor(a/i)
        c = (a-(b*i))*10
        x += str(b)
        e = [0, a]
        while c not in e:
            e += [c]
            b = math.floor(c/i)
            c = (c-(b*i))*10
            x += str(b)
        if c != 0:
            x += str('(')
            a = c
            b = math.floor(c/i)
            c = (c-(b*i))*10
            x += str(b)
            while c != a:
                b = math.floor(c/i)
                c = (c-(b*i))*10
                x += str(b)
            x += str(')')
        if len(f) < len(x):
            f = x
            g = i
    print(g, f)
        
        
