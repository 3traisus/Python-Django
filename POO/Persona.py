class Persona(object):
    def __init__(self,name,sexo,email,fecha_nacimiento,rfc):
        self.__name = name
        self.__sexo = sexo
        self.__email = email
        self.__fecha = fecha_nacimiento
        self.__rfc = rfc
        
    def __str__(self):
        return f"Nombre:{self.__name},Correo:{self.__email},RFC:{self.__rfc}"