'''def fun(a,b):
    yield a+b
    yield a*b
b=fun(3,5)
print(list(b))'''
'''def fun(n):
    a=1
    for _ in range(n):
        yield a
        a*=2
out=fun(10)
print(list(out))'''
def fun(n):
    
    while n>0:
        
        yield n%2
        n=n//2
    
for i in fun(8):
     print(i,end=' ')
