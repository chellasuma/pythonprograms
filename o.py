s='hello world'
b={}
for i in s:
    if not i in b:
        b[i]=1
    else:
        b[i]+=1
print(b)











