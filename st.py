name='Hello world'
b=''

for i in range(len(name)):
    if name[i] in name[i+1:]:
        if name[i] not in b:
            b+=name[i]

     
print(b)