st='hello my name is suma'
b=[]
i=0
temp=' '
while i<len(st):
    if  st[i]!=' ':
        temp+=st[i]
    else:
        b+=[temp]
        temp=' '
        
    i+=1
else:
    if temp:
        b+=[temp]
print(b)

