from abc import ABC,abstractmethod
class modelcar(ABC):
    @abstractmethod
    def Break():
        pass
    @abstractmethod
    def speedup():
        pass
    @abstractmethod
    def speeddown():
        pass
    
#obj=modelcar()
    
class indica(modelcar):
    def __init__(self,speed=0,stop=True):
        self.speed=speed
        self.stop=stop
    #def Break():

    def speedup(self):
         self.speed+=10
         self.stop=False
         print(f'increased by 10 KM {self.speed}')
         
    def Break(self):
        self.speed=0
        self.stop=True
    def speeddown(self):
        if not self.stop:
             self.speed-=10
             if self.speed==0: 
                 self.stop=True
                 print(f'decresed by  10 KM {self.speed}')
        else:
            print('car is in stop mode')
class nexon(modelcar):
    def __init__(self,speed=0,stop=True):
        self.speed=speed
        self.stop=stop
    #def Break():

    def speedup(self):
         self.speed+=5
         self.stop=False
         print(f'increased by 5KM {self.speed}')
         
    def Break(self):
        self.speed=0
        self.stop=True
    def speeddown(self):
        if not self.stop:
             self.speed-=5
             if self.speed==0: 
                 self.stop=True
                 print(f'decresed by 5KM {self.speed}')
        
        

class nexon(modelcar):
    def __init__(self,speed=0,stop=True):
        self.speed=speed
        self.stop=stop
    #def Break():

    def speedup(self):
         self.speed+=5
         self.stop=False
         print(f'increased by 5KM {self.speed}')
         
    def Break(self):
        self.speed=0
        self.stop=True
    def speeddown(self):
        if not self.stop:
             self.speed-=5
             if self.speed==0: 
                 self.stop=True
                 print(f'decresed by 5KM {self.speed}')
        
        


        
        

