a='Hello my name is abhi'
i=0
b=' '
t=True
while i<len(a):
    if a[i]==' ':
        t=True
    elif t and 'a'<=a[i]<='z':
        b+=chr(ord(a[i])-32)
        t=False
    else:
         b+=a[i]
         t=False
    i+=1
print(b)
       
    