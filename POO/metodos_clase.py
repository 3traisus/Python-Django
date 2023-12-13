class Estudiante:
    __contador = 0
    def __init__(self,control,edad,nombre):
        self.__control = control
        self._edad = edad
        self.nombre = nombre
        self.__incrementar()
        
        
    def __str__(self):
        return f"Control:{self.__control}, Nombre {self.nombre}"
    
    @classmethod
    def __incrementar(cls):
        cls.__contador+=1
        
    @property
    def contador(self):
        self.__contador
        
    @property 
    def get_edad(self):
        return self._edad
    
    @edad.setter
    def edad(self,valor):
        self._edad = valor
        

e1 = Estudiante("100",20,"Juan")
print(e1._edad)
e1.edad(18)
print(e1._edad)
print(e1.contador)
