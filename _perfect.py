
s=0
n=int(input('enter number'))
for  i in range(1,n):
    if n%i==0:
        s=s+i
    
if n==s:
     print(n,'perfect number')
else:
    print(n,' not a perfect number')

