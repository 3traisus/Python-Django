'''
Tema: Métodos de clase y estáticos. Encapsulamiento, modificadores de acceso, métodos setter y getter
Fecha: 11 de octubre del 2023
Autor: Leonardo Martínez González
'''
from datos import datos_encuestas

class Encuesta:
    # Variables de clase
    def __init__(self,id, nombre, instrucciones, descripcion, estado):
        self.__id = id
        self.__nombre = nombre
        self.__instrucciones = instrucciones
        self.__descripcion = descripcion
        self.__estado = estado
    def __str__(self):
        return f"ID:{self.__id}, Nombre de encuesta: {self.__nombre}, Instrucciones:{self.__instrucciones}, Estado:{self.__estado}"

    # Getter and Setters
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

# e = Encuesta(100, "A","intrucciones . . . ", "Descripcion . . . ", True)
# e.nombre = "Encuesta B"
# print (e.nombre)

class ListaEncuesta:
    def __init__(self):
        self.__lista_encuestas = []

    def agregar_encuesta(self, encuesta):
        self.__lista_encuestas.append(encuesta)

    def reporte_encuestas(self):
        for encuesta in self.__lista_encuestas:
            print(encuesta)

    def agregar_datos_encuestas(self):
        for encuesta in datos_encuestas:
            id, nombre, instrucciones, descripcion, estado = encuesta.values()
            self.agregar_encuesta( Encuesta( id, nombre, instrucciones, descripcion, estado ) )

class ListaEncuestas:
    def __init__(self):
        self.__lista_encuestas = []
        
    def agregar_encuesta(self,encuesta):
        self.__lista_encuestas.append(encuesta)
        
    def cargar_encuesta(self):
        for encuesta in self.__lista_encuestas:
            self.agregar_encuesta(encuesta)
            
    def reporte_encuesta(self):
        for encuenta in self.__lista_encuestas:
            print(encuenta)
            
lista = ListaEncuesta()
lista.agregar_datos_encuestas()
lista.reporte_encuestas()