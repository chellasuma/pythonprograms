def fact(a,b=1):
    if a==1:
        return
    b*=a
    return fact(a-1,b)
print(fact(6))