a=int(input("enter a value for a:"))
b=int(input("enter a value for b:"))
c=int(input("enter a value for c:"))
if a>b and a>c:
    if b>c:
        print('b is second large')
    else:
         print("c is second large")
elif b>c:

         if a>c:
             print("a is second large")
         else:
               print("c is second large")
elif c>a:
        
    if a>b:
        print("a is second large")
    else:
         print("b is second large")
else:
    
     print("may be a,b and c are equal")
  