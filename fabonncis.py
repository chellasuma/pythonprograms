def frec(a,b=0,c=1,d=()):
    if c>=a: 
        returnd
    elif b==0:
        d+=(b,c)
    else:
        d+=(c,)
    return frec(a,c,b+c,d)
print(frec(100))
print(frec(100))
print(frec(10))