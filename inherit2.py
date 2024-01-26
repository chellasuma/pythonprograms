class gparent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class parent(gparent):
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.c=c
        self.d=d
class child(parent):   
    def __init__(self,a,b,c,d,e,f,):
        super().__init__(a,b,c,d)
        self.e=e
        self.f=f
o=child(1,2,3,4,5,6)