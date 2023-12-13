from Tutor import Tutor
from Estudiante import Estudiante
from Cordinador import Cordinador

class ListaObj():
    def __init__(self):
       self.__lista=[]
       
    def agregar(self,Elemento):
        self.__lista.append(Elemento)
        
    def Mostrar(self):
        for elementos in self.__lista:
            print(elementos)
            
lista = ListaObj()
lista.agregar(Tutor("Jesus","Masculino","jesus@gmail.com","19/02/2001","123","191919","Matematicas","5","19/08/2021",""))
lista.agregar(Tutor("Jesus","Masculino","jesus@gmail.com","19/02/2001","123","191919","Matematicas","5","19/08/2021",""))
lista.agregar(Estudiante("Jesus","Masculino","jesus@gmail.com","19/02/2001","123","19420525","Cetis","Sistemas",19))
lista.agregar(Estudiante("Marta","Femenino","jesus@gmail.com","19/02/2001","234","19420405","CeBetis","Bioquimica",19))   
lista.agregar(Cordinador("Jesus","Masculino","jesus@gmail.com","19/02/2001","123","Sistemas","19/08/2002"))
lista.agregar(Cordinador("Lisa","Femenino","jesus@gmail.com","19/02/2001","234","Bioquimica","19/05/2009"))        
lista.Mostrar()
       