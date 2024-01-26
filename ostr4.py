def str(a,b):
    i=0
    c=''
    while i<len(b):
        if not  b[i] in a:
                c+=b[i] 
        i+=1  
    print(c)  
str('suma','aeiouAEIOU')
    