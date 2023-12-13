class Estudiante:
    #Declaracion de las variables de clase
    
    #Metodo constructor que sirve para inicializar el proyecto
    def __init__(self, control, nombre, sexo, email, fecha_nac, rfc, escuela_pro):
        #Variables de instancia
        self.control = control
        self.nombre = nombre
        self.sexo = sexo
        self.email = email
        self.fecha_nac = fecha_nac
        self.rfc = rfc
        self.esxuela_pro = escuela_pro
        self.estado = True
        
    #Metodo especial _str_(self)
    def __str__(self):
        return f"Control: {self.control}, Nombre:{self.nombre}, Email:{self.email}, Estado:{self.estado}"
    #Metodo de instancia
    def Cambiar_Estado(self):
        self.estado = not self.estado

class Lista_Estudiante:
    def _init_(self):
        self.lista_estudiantes = []

    #Metodo de instancia Agregar_Estudiante
    def agregar_estudiante(self, estudiante):
        #Verificar que no este repetido el estudiante
        indice = self.buscar_estudiante(estudiante.control)
        if indice == -1:
            self.lista_estudiantes.append(estudiante)
            return True
        else:
            return False

    #Metodo de instancia para buscar un Estudiante
    def buscar_estudiante(self, ctrl):
        posicion = 0
        for estudiante in self.lista.estudiantes:
            if ctrl == estudiante.control:
                return posicion
            posicion +=1
        return -1 #No existe el estudiante en la lista
        
        #Metodo de instancia
        

objeto_estudiante = Estudiante("18420100","David", "Masculino", "jf90221@gmail.com", "27/02/2001", "1232123", "Tecnologico Jiquilpan")
print(object.__str__)
#print(objeto_estudiante)
#objeto_estudiante.Cambiar_Estado()
#print(objeto_estudiante)