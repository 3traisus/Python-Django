from datos import datos_respuestas
class Respuesta:
    def __init__(self, id_respuesta, id_pregunta, titulo_respuesta):
        self.__id_respuesta = id_respuesta
        self.__id_pregunta = id_pregunta
        self.__titulo_respuesta = titulo_respuesta

    def __str__(self):
        return f"ID Respuesta:{self.__id_respuesta}, ID Pregunta:{self.__id_pregunta}, Respuesta:-{self.__titulo_respuesta}"


class ListaRespuestas:
    def __init__(self):
        self.__lista_respuestas = []

    def agregar_respuesta(self, respuesta):
        self.__lista_respuestas.append( respuesta )

    def cargar_respuestas(self):
        for respuesta in datos_respuestas:
            self.agregar_respuesta(respuesta)
        
    def reporte_respuestas(self):
        for respuesta in self.__lista_respuestas:
            print(respuesta)
            
lista_respuestas = ListaRespuestas()
lista_respuestas.cargar_respuestas()
lista_respuestas.reporte_respuestas
        