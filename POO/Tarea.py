import Recursos.MongoBD as MongoBD
import Recursos.Listas_Tuplas_Conjuntos_Dicc as ltc
from datos_practica import datos_respuestas_usuario, data

def ValidarUser(func):
    def wrapper(*args,**kwargs):
        tabla = MongoBD.seleccionar_Collec_Tabla(MongoBD.conectar_mongo("localhost","27017",True),"Encuesta_4","Usuario")
        lista = MongoBD.Consulta(tabla)
        usuario_valido = False
        for elemento in lista:
            print(elemento["clv"],args[0])
            if elemento["clv"] == args[0]:
                usuario_valido = True
                break
        if usuario_valido:
            return func(*args, **kwargs)
        else:
            return "Acceso Denegado"
    return wrapper
     
@ValidarUser 
def Usuario(clv):
    tabla = MongoBD.seleccionar_Collec_Tabla(MongoBD.conectar_mongo("localhost","27017",True),"Encuesta_4","Usuario")
    lista = MongoBD.Consulta(tabla)
    for elemento in lista:
        if elemento["clv"] == clv:
            return elemento["nombre"]

class Resultado:
    def __init__(self,clv):
        self.__crt = clv
        self.__nombre = Usuario(clv)
        
    def Json(self):
        listaval = []
        if self.__nombre != "Acceso Denegado":
            for datos in datos_respuestas_usuario:
                if datos["control"] == self.__crt:
                    listaval.append(datos["valor"])
        data["control"] = self.__crt
        data["nombre"] = self.__nombre
        data["resultados"] = ltc.New_diccionario(["uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez"],listaval)
        return data
           
r = Resultado("18420455")
print(r.Json())
      
    
