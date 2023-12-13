from Persona import Persona
class Cordinador(Persona):
    def __init__(self, name, sexo, email, fecha_nacimiento, rfc,programa,fecha_nombramiento):
        super().__init__(name, sexo, email, fecha_nacimiento, rfc)   
        self.__programa = programa
        self.__nombra = fecha_nombramiento
        
    def __str__(self):
        cad1 = super().__str__()
        cad2 = "\nDatos Cordinador:\n"
        cad2 = cad2 + f"Programa:{self.__programa},Nombremiento:{self.__nombra}"
        return cad1 + cad2
