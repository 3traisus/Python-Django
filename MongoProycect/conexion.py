import pymongo
import pymongo.errors 
import json

def conectar_mongo(Mongohost="localhost",Mongopuerto="27017",Mongodb="itj_est"):
    #cadena de conexion
    
    mongo_uri= f"mongodb://{Mongohost}:{Mongopuerto}/"
    mongo_client = pymongo.MongoClient(mongo_uri)
    try:
        return mongo_client[Mongodb]
    #except OperationFailure as error_operacional:
     #   return "Error en la operacion:",error_operacional
    except pymongo.errors.ServerSelectionTimeoutError as ErrorTiempo:
        return "Tiempo Excedido para la conexion", ErrorTiempo

def consulta_mongo(conexion,db,tabla,filtro,atributos={"_id":0}):
    data=[]
    try:
        respuesta = conexion[db][tabla].find(filtro,atributos)
        if respuesta:
            for registro in data:
                data.append(registro)
    except NameError as error:
        print(error)
    else:
        respuesta.close()
        return json.dumps(data)

conectar = conectar_mongo()
print(consulta_mongo(conectar,db="itj_est",tabla="estudiantes",filtro={}))
    