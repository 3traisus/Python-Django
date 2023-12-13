from decouple import config
import pymongo 
import pymongo.errors 
import Recursos.Listas_Tuplas_Conjuntos_Dicc as ltc

class Mongo:
    def __init__(self,Mongohost,Mongopuerto):
        self.mongohost = Mongohost
        self.mongo_puerto = Mongopuerto
        self.mongo_cliente = None
        self.tabla = None
        self.collect = None
        self.MONGO_URI = mongo_uri= f"mongodb://{Mongohost}:{Mongopuerto}/"  if Mongohost.lower() == "localhost" else config('MONGO_URI')
        
    #Metodo de instacia
    def conectar_mongo(self):
        try:
            self.mongo_cliente = pymongo.MongoClient(self.MONGO_URI)
        except pymongo.errors.ServerSelectionTimeoutError as ErrorTiempo:
            return "No Exito"
        return "Exito"
    
    def set_Collec_Tabla(self,nametabla,namecollect):
        try:
            self.collect = self.mongo_cliente[nametabla]
            self.tabla = self.collect[namecollect]
        except Exception:
            return "Error"
        
    def Consulta(self):
        lista = []
        registro = self.tabla.find()
        for datos in registro:
            lista.append(datos)
        return lista
    
    def Insertar_one(self,**kwargs):
        self.tabla.insert_one(kwargs)
        
    def Eliminar_one(self,filtro_dic):
        self.tabla.delete_one(filtro_dic)
        
    def Update_one(self,new_dic,filtro_dic):
        nuevos_valores = {"$set": new_dic}
        self.tabla.update_one(filtro_dic, nuevos_valores)
    
conn = Mongo("localhost","27017")
conn.conectar_mongo()
conn.set_Collec_Tabla("itj_est","estudiantes")
print(conn.MONGO_URI)
name = "Yael Joto"
control = "19420525"
#conn.Eliminar_one({"nombre":name})
#conn.Insertar_one(nombre=name,control=control)
#conn.Update_one({"nombre":"Yael XD","control":19420525},{"nombre":name})
