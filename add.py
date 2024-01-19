a=[1,'1',2,2.4,[4,5,6],9,16,'abcd']
b=0
for i in a:
    if  type(i)==int:
        if i%2==0:
            b=b+i
        else:
            b=b-i
    
print(b)
