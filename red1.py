
from functools import reduce
a=[1,2,3,4,5]
b=map(lambda x:x**2,a)
print(reduce(lambda x,y:x+y,b ))

