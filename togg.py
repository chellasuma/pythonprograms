def tog():
    a=input('enter string')
    b=''
    i=0
    y=''
    while i<len(a):
        if 'a'<=a[i]<='z':
            b+=chr(ord(a[i])-32)
        elif 'A'<=a[i]<='Z':
           b+=chr(ord(a[i])+32)
        
        else:
         b+=a[i]
        i+=1
                                                                                                                                                                                                                                                                                                                                                      d    
    return b
print(tog())