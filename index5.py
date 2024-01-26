def index2(a):
    b=[]
    i=0
    while i<len(a):
        if a[i] in 'aeiouAEIOU':
            b+=[i]
        i+=1
    print(b)
    return b
print(index2('suma'))