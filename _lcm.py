a=int(input('enter a;-'))
b=int(input('enter b;-'))

if a>b:
    m=a
else:
    m=b
while(True):
    if m%a==0 and m%b==0:
        print('LCM=',m)
        break
    m+=1
c=(a*b)//m
print('hcf=',c)