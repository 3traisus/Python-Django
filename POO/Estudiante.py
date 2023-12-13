from Persona import Persona
class Estudiante(Persona):
    def __init__(self,name,sexo,email,fecha_nacimiento,rfc,control,precedencia,carrera,edad):
        super().__init__(name,sexo,email,fecha_nacimiento,rfc)
        self.__control = control
        self.__procedencia = precedencia
        self.__carrera = carrera
        self.__edad = edad
        self.__estado = True
        
    def __str__(self):
        cad1 = super().__str__()
        cad2 = "\nDatos Escolares:\n"
        cad2 = cad2 + f"Control:{self.__control},Carrera:{self.__carrera},Estado:{self.__estado}"
        return cad1 + cad2
    
    def actualizar(self,valor):
        self.__edad = valor
        
    def udp_estado(self):
        self.__estado = not self.__estado
        