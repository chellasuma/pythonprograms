class mtca:
    chairman='mr sunil'
    location='plmr'
    def __init__(self,name,sem):
        self.name = name
        self.sem = sem
class mca(mtca):
    principal='mr prabhakar sir'
    staff=45
    
class betech(mtca):
    principal='sudha'
    staff=39
s1=mca('suma',1)
s2=betech('priya',4)