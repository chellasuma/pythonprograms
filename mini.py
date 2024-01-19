print(" 1 ----> chennai \n 2 ----->delhi \n 3 ----->mumbai \n 4 ----->hyderabad)")
destintion =input("enter destination:")
seats=int(input("enter number of seats:"))
adults=int(input("enter number of adults:"))
children=int(input("enter number of children:  "))
acclassadults=int(input("enter number of ac seats for addults"))
acclasschild=int(input("enter number of ac seats for children"))
nonacclassadults=int(input("enter number of nonac seats for adults"))
nacclasschild=int(input("enter number of nonac seats for children"))
aca =10
acc=5
naca=5
nacc=3

if destintion in '1':
    
     price=350*(acclasschild*acc+nacclasschild*nacc)*children + 350*(acclassadults*aca+nonacclassadults*acc)*adults
    
     print(price)
     print("thanks for visiting")
elif destintion in '2':
    price=2000*(acclasschild*acc+nacclasschild)*children + 2000*(acclassadults*aca+nonacclassadults*acc)*adults
    print(price)
    print("thanks for visiting")
elif destintion in '3':
    price=800*(acclasschild*acc+nacclasschild)*children + 800*(acclassadults*aca+nonacclassadults*acc)*adults
    print(price)
    print("thanks for visiting")
elif destintion in '4':
    price=500*(acclasschild*acc+nacclasschild)*children + 500*(acclassadults*aca+nonacclassadults*acc)*adults
    print("total price:" + price)
    print("thanks for visiting")
      