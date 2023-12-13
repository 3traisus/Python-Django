import pymongo
import pymongo.errors 
import json

def conectar_mongo(Mongohost,Mongopuerto,booleanservidor):
    if booleanservidor:
        mongo_uri= f"mongodb://{Mongohost}:{Mongopuerto}/"
        mongo_client = pymongo.MongoClient(mongo_uri)
    else:
        mongo_uriservidor = "mongodb+srv://jesusnuez021:H6XYqd3y3NyN3IjR@cluster0.vzwuwzq.mongodb.net/"
        mongo_client = pymongo.MongoClient(mongo_uriservidor)
    try:
        return mongo_client
    except pymongo.errors.ServerSelectionTimeoutError as ErrorTiempo:
        print("Tiempo Excedido para la conexion", ErrorTiempo)
        
def seleccionar_Collec_Tabla(db,nametabla,namecollect):
    collect = db[nametabla]
    tabla = collect[namecollect]
    return tabla

def Consulta(tabla):
    lista = []
    registro = tabla.find()
    for datos in registro:
        lista.append(datos)
    return lista

def Insertar_one(tabla,**kwargs):
    tabla.insert_one(kwargs)
    
def Insertar_varios(tabla,list_dic):
    tabla.insert_many(list_dic)
    
def Eliminar_one(tabla,filtro_dic):
    tabla.delete_one(filtro_dic)
    
def Eliminar_varios(tabla,filtro_dic):
    tabla.delete_many(filtro_dic)   
    
def Update_one(tabla,new_dic,filtro_dic):
    nuevos_valores = {"$set": new_dic}
    update_result = tabla.update_one(filtro_dic, nuevos_valores)

def Update_varios(tabla,new_dic,filtro_dic):
    nuevos_valores = {"$set": new_dic}
    update_result = tabla.update_one(filtro_dic, nuevos_valores)    

def extraer_info_ele(registro,pos,atributo):#Extra un campo del registro
    return registro[pos][atributo]