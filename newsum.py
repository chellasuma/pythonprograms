def sum6(a,s):
    i=0
    if  len(str((a)==6)):
        while i<a:
            d=a%10
            if d%2 == 0:
               s=s+d
            a=a//10
            i+=1
    print(s)
    return s

print(sum6(444444,0))