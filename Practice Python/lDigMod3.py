def mod(n):
    if int(n/10)==0 and n%3 == 0:
        return int(n)
    return 0
def mod2(l):
    if int(l/10)==0 :
        return mod(l)
    if (mod(l%10))!=0 :
        return int(mod(l%10))+ mod2(int(l/10))*10
    else :
        return int(mod(l%10))+ mod2(int(l/10))
print(mod2(674208934208))
