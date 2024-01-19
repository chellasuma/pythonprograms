i=1

n=int(input('enter a number'))
c=0
while i<n//2:
    if n%1==0:
        c+=1
    i+=1
if c==2:
    print('prime')
else:
    print('not prime')