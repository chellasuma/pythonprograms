class parant:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def display(self):
        print(self.a,self.b)
class child(parant):
    pass
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.c = c
        self.d= d
    def display(self):
        super().display()
        print(self.c,self.d)
o=child(3,5,7,9)
        