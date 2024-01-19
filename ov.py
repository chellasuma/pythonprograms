a='aeiousuma'
i=0
b=[]
for i in range(len(a)):
    if  a[i] in 'aeiouAEIOU':
        b=b+[i]    
    
print(b)