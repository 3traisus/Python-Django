from decouple import config
import pymongo
from pymongo.errors import OperationFailure


class Mongo:
    # Variables de clase
    def __init__(self, MONGO_HOST="localhost", MONGO_PORT="27017", MONGO_DB="Encuesta_4"):
        self.MONGO_HOST = MONGO_HOST
        self.MONGO_PORT = MONGO_PORT
        self.MONGO_DB = MONGO_DB
        self.MONGO_CLIENT = None
        # Cadena de conexion
        self.MONGO_URI = f"mongodb://{self.MONGO_HOST}:{self.MONGO_PORT}/" if MONGO_HOST.lower() == 'localhost' else config('MONGO_URI')

    # Método de instancia conectar
    def conectar(self):
        try:
            self.MONGO_CLIENT = pymongo.MongoClient(self.MONGO_URI)
            try:
                print(self.MONGO_CLIENT.server_info())
                return "Conexion exitosa"
            except OperationFailure as error_operacion:
                return "Error en la operación: " + str(error_operacion)
        except pymongo.errors.ServerSelectionTimeoutError as error_tiempo:
            return "Tiempo excedido para la conexion " + str(error_tiempo)

    # Método de instancia para consultar colecciones en MOngoDB
    def consulta(self, tabla, filtro):  # , atributos={"_id":0}
        response = {'bandera':False, 'mensaje':'No existen registros', 'data': []}
        try:
            respuesta = self.MONGO_CLIENT[self.MONGO_DB][tabla].find(filtro)  # , atributos
            if respuesta:
                for registro in respuesta:
                    response['data'].append(registro)
                # response['bandera'] = True
                # response['mensaje'] = 'Consulta realizada con éxito'
        except NameError as error:
            print(error)
        else:
            respuesta.close()
        return response  # json.dumps

    # Método de instancia insertar documentos en MongoDB
    def insertar(self, tabla, documento):
        respuesta = self.MONGO_CLIENT[self.MONGO_DB][tabla].insert_one(documento)  # insert_many([{ ... }, { ... }])
        if respuesta:
            return respuesta
        else:
            return None

    # Método de instanciapara eliminar documentos en MongoDB
    def eliminar(self, tabla, filtro):
        respuesta = self.MONGO_CLIENT[self.MONGO_DB][tabla].delete_one(filtro)  # delete_many(filtro)
        if respuesta:
            return respuesta
        else:
            return None

        # Método de instancia modificar documentos en MongoDB
    def modificar(self, tabla, filtro, datos):
        respuesta = self.MONGO_CLIENT[self.MONGO_DB][tabla].update_one(filtro, datos)  # update_many([{ ... }, { ... }])
        if respuesta:
            return respuesta
        else:
            return None

conn = Mongo()
conn.conectar()
filtro = {"_id": 100}
conn.consulta("Usuario",{"nombre":"Jesus Eduardo"})