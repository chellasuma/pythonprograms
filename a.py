a=int(input("enter vaiue for a"))
b=int(input("enter vaiue for b"))
c=eval(input("enter operator"))

if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)

elif c=='*':
    print(a*b)
elif c=='%':
    print(a%b)
elif c=='**':
  print(a**b)
elif c=='/':
    print(a/b)
elif c=='//':
    print(a//b)
else:
    print('invalid operator')

