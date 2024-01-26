a=[4,4,'abc',[1,2,3,4]]
#out={ i:a[i] for i in range(len(a))}
out={i:j for i,j in enumerate(a)}
print(out)
