'''
def mi_funcion():
    print("Esta es mi función")

mi_funcion()

def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes de ejecutar la función")
        resultado = func(*args, **kwargs)
        print("Después de ejecutar la función")
        return resultado
    return wrapper

@mi_decorador
def otra_funcion():
    print("Esta es otra función")

otra_funcion()'''

'''
class Usuer():
    def __init__(self,usr,rol):
        self.__ROLES = {
            'Admin':['Panel Administrador','Admon Usuarios'],
            'user': ['Contenido vistas']
        }
        self.__USERS = {'usuario':usr,'rol':rol}
        
    def __str__(self):
        print(f"User:{self.__ROLES['user']}, Rol:{self.__ROLES['Admin']}")
        
        
    def Rol_return(self):
        return self.__ROLES[self.__USERS['rol']]
    
    def users(self):
        return self.__USERS['usuario']

class ListaUser():
    def __init__(self):
        self.__lista = []
        
    def Agregar_user(self,elemento):
        self.__lista.append(elemento)
        
    def Reporte_usuarios(self):
        for elemento in self.__lista:
            print(elemento)
            
    def regresa_usuario(self):
        return self.__lista
    

lista = ListaUser()
u1 = Usuer("Piter","Admin")
print(u1.Rol_return())
lista.Agregar_user(u1)
lista.Agregar_user(Usuer("Mary","user"))

lista.Reporte_usuarios()


@autorizar_por_rol(lista,u1)
def accion_admin():
    print("Entro al metodo accion_admin")

def autorizar_por_rol(lista,usr):
    def decorador(func):
        def wrapper (*args,**kwargs):
            for usuarios in lista:
                if usuarios == usr:
                    print (usuarios)
            return func (*args,**kwargs)
        return wrapper
    return decorador

autorizar_por_rol(lista.regresa_usuario(),"Piter")'''


'''Crear un decorador que valide datos de entrada de una funcion:
    Validar que los argumentos sean numeros positivos'''
#Funcion decoradora que valide numeros positivos

def validad_numeros_positivos(func):
    def wrapp(*args,**kwargs):
        for argumento in args:
            if not isinstance(argumento,(float,int)) or argumento <=0:
                return "Los argumentos deben ser numeros posisitivos"
        return func (*args,**kwargs)  
    return wrapp

#Funcion que regrese el area de un rectangulo
@validad_numeros_positivos
def calcular_area_rec(alto,ancho):
    return alto * ancho

print(calcular_area_rec(5,5))