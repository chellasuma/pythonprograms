'''a=[1,0,True,'','str',[1,2,3],0.0,78]
#out=[i for i in a if bool(i) ]
filter(bool,a)
out=list(filter(bool,a))
print(out)'''
b=[2,56,6,7,87,9,65,9,9,99,66,27]
'''def mul(n):
    if n%3==0:
        return True
    else:
        return False
filter(mul,b)
out=list(filter(mul,b))
print(out)'''
print(list(filter(lambda n:n%3==0,b)))