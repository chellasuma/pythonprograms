a=8
out=''
temp=''
for i in range(a):
    for j in range(a):
        if i in [j,a-j-1,temp] or j in [temp]:
            out+='*'
        else :
            out+=' '
    out+='\n'
print(out)