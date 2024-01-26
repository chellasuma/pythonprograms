def recp(n,i=2):
    if n==i:
         return 'prime'
    elif n%i==0 :     
         return ' not prime'
    return recp(n,i+1)
print(recp(5))
    