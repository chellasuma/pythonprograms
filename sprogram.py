a='Hello my name is abhi'
i=0
b=' '
while i<len(a):
    if a[i]==' ':
        b+='_'
    else:
        b+=a[i]
    i+=1

print(b)