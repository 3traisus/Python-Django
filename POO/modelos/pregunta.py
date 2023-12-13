from datos import datos_preguntas

class Pregunta:
    def __init__(self, id_pregunta, id_encuesta, numero_pregunta, titulo_pregunta ):
        self.__id_pregunta = id_pregunta
        self.__id_encuesta = id_encuesta
        self.__numero_pregunta = numero_pregunta
        self.__titulo_pregunta = titulo_pregunta

    def __str__(self):
        cad = f"ID Pregunta:{self.__id_pregunta}, ID Encuesta:{self.__id_encuesta} "
        cad += f"Num. Pregunta: {self.__numero_pregunta}, Pregunta:{self.__titulo_pregunta}"
        return cad


class ListaPreguntas:
    def __init__(self):
        self.__lista_preguntas = []

    def agregar_pregunta(self, pregunta):
        self.__lista_preguntas.append(pregunta)

    def cargar_preguntas(self):
        for pregunta in datos_preguntas:
            id_pregunta, id_encuesta, numero_pregunta, titulo_pregunta = pregunta.values()
            self.agregar_pregunta( Pregunta(id_pregunta, id_encuesta, numero_pregunta, titulo_pregunta) )

    def reporte_preguntas(self):
        for pregunta in self.__lista_preguntas:
            print(pregunta)


listap = ListaPreguntas()
listap.cargar_preguntas()
listap.reporte_preguntas()