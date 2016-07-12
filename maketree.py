import random

def supsub(sups, subs, c = "e"):
    return c+"^{"+sups+"}"+"_{"+subs+"}"
           
def pyramid(u,d = 0,c="e"):
    if u == d == 0:
        return c
    if u == 0 and d > 0:
        return supsub("",pyramid(0,d-1),c)
    if d == 0 and u > 0:
        return supsub(pyramid(u-1,d+1),"",c)
    else:
        return supsub(pyramid(u-1,d+1),pyramid(0,d-1),c)

def tree(p=.5,c="e"):
    if p > random.random():
        top = tree(p)
    else:
        top = ""
    if p > random.random():
        bottom = tree(p)
    else:
        bottom = ""
    return supsub(top,bottom)

def minsizetree(s):
    while 1:
        try:
            t = tree()
            if 2*s > t.count("e") > s:
                return t
        except:
            pass


def forest(s=94,n=4):
    return ''.join([minsizetree(random.randint(s/2,s)) for i in range(n)])
        
