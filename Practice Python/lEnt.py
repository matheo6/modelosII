def lEnt(l):
    if (l-int(l))==0:
        return l
    return lEnt(l*10)
def kl(l):
    if(l==[]):
        return 0
    return lEnt(l[0])+ kl(l[1:])
print(kl([8.44,7.233,6.4]))
