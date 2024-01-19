a=eval(input("enter character"))
if a in "0123456789":
    print("digit")
elif a>='A' and a<='Z':
    print("uppercase")
elif a>='a' and a<='z':
    print("lowercase")
else:
    print("special")
    