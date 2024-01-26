class mtca:
    principal_n='prabakhr sir'
    college_n='mother tesisa'
    location='palamaner'
    def __init__(self,sn,c,mn,ma,s):
        self.sname=sn
        self.course=c
        self.mno=mn
        self.mail=ma
        self.sem=s
    def updatemno(self,new):
        self.mno=new
        print('updated')
    def updatecourse(self,new):
        self.course=new
    def updatemail(self,new):
        self.mail=new
        print('updated')
    def updatesem(self,new):
        self.sem=new
    @classmethod
    def changeprincipal(cls,new):
        cls.principal_n=new
    @staticmethod
    def sum(a,b):
        return a+b


student=mtca('suma','mca',6390885443,'sumachela2@gmail',1)

