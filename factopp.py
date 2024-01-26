def factopp(a,n=1):
     if a==n:
        return 1 
     return a*factopp(a-1)
print(factopp(6))