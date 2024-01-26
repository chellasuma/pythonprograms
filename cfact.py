

def fact5(num):
    out=1
    for _ in range(1,num+1):
        out*=_
    return out
out=[fact5(i) for i in range(1,11) if i%2==0]
print(out)

        

