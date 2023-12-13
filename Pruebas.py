import Recursos.MongoBD as mongodb
import Recursos.Listas_Tuplas_Conjuntos_Dicc as ltc
import Recursos.DataBase as db

'''
conn = mongodb.conectar_mongo("localhost","27017")
tabla = mongodb.seleccionar_Collec_Tabla(conn,"itj_est","estudiantes")
registro = mongodb.Consulta(tabla)
#mongodb.Insertar_varios(tabla,ltc.Lista_diccionario(["nombre","control","nombre","control"],["JESUS","19420525","CECI","19420528"],2,))
#mongodb.Insertar_one(tabla,nombre="Jesus",control="19420525")
#dato = mongodb.extraer_info_ele(registro,2,"_id")
#mongodb.Eliminar_one(tabla,{"_id":{"$eq":dato}})
'''

#conn,cursor=db.sqlserver_connection(server="DESKTOP-NPGL15G",database="NATURISTADEFINITIVA",username="",password="")
#print(db.sqlserver_Consulta(cursor,"SELECT * FROM EMPLEADO"))
#print(db.sqlserver_Accion(cursor,conn,"SELECT * FROM EMPLEADO"))


