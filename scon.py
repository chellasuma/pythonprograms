a='sumamca'
i=0
b=' '
while i<len(a):
    if 'a'<=a[i]<='z':
        b+=chr(ord(a[i])-32)

    else:
        b+=a[i]
    i+=1
print(b)