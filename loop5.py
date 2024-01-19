a=input('enter string :-')
i=-1
c=0
while i>=-len(a):
    if a[i] in 'aeiouAEIOU':
        c=c+1
    i-=1
print(c)
