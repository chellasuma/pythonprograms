class bank:
    bankname='SBI'
    managername='ravi'
    IFSCcode=234544454
    branchname='pamnr'
    def __init__(self,name,acno,pan,audhar,dob,balance):
        self.name = name
        self.acno = acno
        self.pan = pan
        self.audhar = audhar
        self.dob=dob
        self.balance=balance
    def credit(self,amt):
         self.balance+=amt
    def debit(self,amt):
        if self.balance>=amt:
         self.balance-=amt
        else:
            print("insufficient balance")
    def checkbalance(self):
        return self.balance
    @classmethod
    def changebranch(cls,new):
        cls.branchname=new
    @classmethod
    def changemanager(cls,new):
        cls.manager=new
acholder1=bank('suma',42432,45454,3435,'30/8/2003',5000)

    
