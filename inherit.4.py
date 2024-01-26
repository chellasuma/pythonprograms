class add:
    @staticmethod
    def add2(a,b):
        return a+b
    @staticmethod
    def add3(a,b,c):
        return a+b+c
class sub():
    @staticmethod
    def sub(a,b):
        return a-b                  
class cal(add,sub):
    pass
obj=cal()
print(obj.add2(3,5))
print(obj.sub(2,5))

