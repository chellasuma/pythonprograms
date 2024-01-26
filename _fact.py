def fact1():
    b=1
    a=int(input("enter a number:"))
    for i in range(1,a):
        b*=i
    print(b)
fact1()