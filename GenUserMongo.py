import Recursos.MongoBD as mongodb
import Recursos.Listas_Tuplas_Conjuntos_Dicc as ltc
from faker import Faker
import random as rar
import re 
import bcrypt as cryp
import json


def Password(tam):
   minus=["a","b","c","d","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
   mayus=["A","B","C","D","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
   carac =["@","#","?","%","&","$","_","!"]
   num = ["0","1","2","3","4","5","6","7","8","9"]
   lenguaje=[]
   pas =""
   lenguaje.extend(minus)
   lenguaje.extend(mayus)
   lenguaje.extend(carac)
   lenguaje.extend(num)
   for x in range(0,tam):
      pas += rar.choice(lenguaje)
   pas +=""
   if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$%&_?!#])',pas):
       return pas
   else:
       return Password(tam)
    
def hash_password_bcrypt(password):
    hashed = cryp.hashpw(str(password).encode('utf-8'), cryp.gensalt())
    return hashed

def Gen_user(num_user,clv):
    fake = Faker()
    listaClave =[]
    listaValor = []
    for x in range(num_user):
        listaClave.extend(clv)
        listaValor.append(fake.name())
        listaValor.append(fake.email())
        contra = Password(10)
        listaValor.append(contra)
        listaValor.append(hash_password_bcrypt(contra))
    return listaClave,listaValor

def Validacion(passw,reg):
    for datos in reg:
        if cryp.checkpw(passw,datos["P_cifrada"]):
            print(f"Bienvenido: {datos['Username']}")

conn = mongodb.conectar_mongo("localhost","27017",True)
tabla = mongodb.seleccionar_Collec_Tabla(conn,"Usuarios","Datos")
lc,lv = Gen_user(5,["Username","Correo","Password","P_cifrada"])
mongodb.Insertar_varios(tabla,ltc.Lista_diccionario(lc,lv,4,))

#registro = mongodb.Consulta(tabla)
#contra = "x0S$p&%@Ty".encode('utf-8')
#Validacion(contra,registro)
    


'''
def guardar_json():
    lc,lv = Gen_user(3,["Username","Correo","Password","P_cifrada"])
    print(f"{lc}/{lv}")
    with open("Datos.json","w") as archivo:
        archivo.writelines(ltc.Lista_diccionario(lc,lv,4,))
        
guardar_json()
'''
        
    
    


    