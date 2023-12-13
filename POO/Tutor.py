from Persona import Persona
class Tutor(Persona):
    def __init__(self, name, sexo, email, fecha_nacimiento, rfc,num_tar,grupo,periodo,fecha_nombramiento,tipo):
        super().__init__(name, sexo, email, fecha_nacimiento, rfc)
        self.__num_tar = num_tar
        self.__grupo = grupo
        self.__periodo = periodo
        self.__fecha = fecha_nombramiento
        self.__tipo = tipo
        
    def __str__(self):
        cad1 = super().__str__()
        cad2 = "\n Datos tutot\n"
        cad2 = cad2 + f"Tarjeta:{self.__num_tar},Grupo:{self.__grupo},Fecha Nombramiento:{self.__fecha},Periodo:{self.__periodo}"   
        return cad1 +cad2