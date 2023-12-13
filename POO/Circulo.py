class Circulo:
    
    def __init__ (self,radio):
        self.radio = radio
        
    def area(self):
        return self.pi()*self.radio**2
    
    @staticmethod
    def pi():
        return 3.1416
    
cir = Circulo(4)
print(cir.area())
print(cir.pi())