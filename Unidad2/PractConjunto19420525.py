'''
Tema: Aplicación de estructuras de Python: archivos, JSON, cifrado de contraseñas
Fecha: 07 de septiembre del 2023
Autor: Leonardo Martínez González

'''





#Crear un programa que utilice los archivos Estudiantes.txt y kardex.txt:

#1. Crear un método que regrese un conjunto de tuplas de estudiantes.
#   La tupla debe contener (control, nombre). (5) 10 min.

def crear_Conjunto_est():
    conjunto = set ()
    with open("Estudiantes.txt","r") as archivo:
        for linea in archivo:
            control = linea.split("|")[0]
            nombre =  linea.split("|")[1][:-1]
            conjunto .add((control,nombre))
    return conjunto
#cad.Strip() Elimina espacios en blanco
print(crear_Conjunto_est())
            
   
#2. Crear un método que regrese un conjunto de tuplas de materias.
#   La tupla debe contener (control, materia, promedio).
def crear_Conjunto_Prom():
    conjunto_prom = set ()
    with open("Kardex.txt","r") as archivo:
        for linea in archivo:
            control = linea.split("|")[0]
            nombre =  linea.split("|")[1]
            promedio = linea.split("|")[2][0:-1]
            conjunto_prom.add((control,nombre,promedio))
    return conjunto_prom
#cad.Strip() Elimina espacios en blanco
print(crear_Conjunto_Prom())
#3. Crear un método que dado un número de control regrese el siguiente formato JSON:
'''{
        "Nombre": "Manzo Avalos Diego",
        "Materias":[
            {
                "Nombre":"Base de Datos",
                "Promedio":85
            },
            {
                "Nombre":"Inteligencia Artificial",
                "Promedio":100
            },
            . . . 
        ],
        "Promedio general": 98.4
   }'''
   
def New_diccionario(claves,valor):
    dic = dict.fromkeys(claves)
    if len(valor)>0:
        for clav in enumerate(claves):
            dic[clav[1]] = valor[clav[0]]
    return dic
   
def crear_conjunto_estudiante(ctrl):
    estud = crear_Conjunto_est()
    prom = crear_Conjunto_Prom()
    materias=[]
    promedios=[]
    for est in estud:
        if est[0]==ctrl:
            name = est[1]
            break
    for pro in prom:
        if est[0]==ctrl:
            materias.append(pro[1])
            promedios.append(int(pro[2]))
    
    calProm = sum(promedios)/len(promedios)
    Diccion = New_diccionario(["Nombre","Materias","Promedio"],[name,New_diccionario(materias,promedios),calProm])
    return Diccion

print("/////////////////////////////////////////////////////////////////////")
print(crear_conjunto_estudiante("18420427"))

'''
4. Regresar una lista de JSON con las materias de un estudiante, el formato es el siguiente:
[
    {"Nombre": "Contabilidad Financiera"},
    {"Nombre": "Dise\u00f1o UX y UI"}, 
    {"Nombre": "Base de datos distribuidas"}, 
    {"Nombre": "Finanzas internacionales IV"}, 
    {"Nombre": "Analisis y dise\u00f1o de sistemas de informacion"}, 
    {"Nombre": "Microservicios"},
    {"Nombre": "Algoritmos inteligentes"}
]
'''

def Json_Materias(ctrl):
    mat = crear_Conjunto_Prom()
    nombre = []
    for est in mat:
        if est[0]==ctrl:
            nombre.append(New_diccionario(["Nombre"],[est[1]]))
    return nombre   
        
print("/////////////////////////////////////////////////////////////////////")
print(Json_Materias("18420427"))

'''
5. Generar un archivo de usuarios que contenga el numero de control, éste será el usuario
   y se generará una contraseña de tamaño 10 la cual debe tener:
   A. Al menos una letra mayúscula 
   B. Al menos una letra minúscula
   C. Numeros
   D. Al menos UN carácter especial, considere ( @, , $,%,&,_,?,! )'''

import re as re
import random as rar
import bcrypt as cryp

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

def Generar_user():
    lista=[]
    estudianteControl = crear_Conjunto_est()
    for crtl in estudianteControl:
        contraseña = Password(10)
        passCifra = hash_password_bcrypt(contraseña)
        lista.append(f"{crtl[0]}|{contraseña}|{passCifra}\n")
    with open ("User.txt","w") as archivo:
        archivo.writelines(lista)
        
#Generar_user() 
'''
   Considere:
    - Crear un método para generar cada caracter
    - El codigo ascii: https://elcodigoascii.com.ar/
    - Cifrar la contraseña con bcrypt, se utiliza con node.js, react, etc. Para ello:
        * Descargue la libreria bcrypt con el comando: "pip install bcrypt" desde la terminal o desde PyCharm
        * Página: https://pypi.org/project/bcrypt/
        * Video:Como Cifrar Contraseñas en Python     https://www.youtube.com/watch?v=9tEovDYSPK4

   El formato del archivo usuarios.txt será:
   control contrasena contraseña_cifrada'''

'''
6. Crear un método "autenticar_usuario(usuario,contrasena)" que regrese una bandera que 
   indica si se pudo AUTENTICAR, el nombre del estudiante y un mensaje, regresar el JSON:
   {
        "Bandera": True,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Bienvenido al Sistema de Autenticación de usuarios"
   }

   ó

   {
        "Bandera": False,
        "Usuario": "",
        "Mensaje": "No existe el Usuario"
   }

   ó

    {
        "Bandera": False,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Contraseña incorrecta"
   }
   '''
def crear_Conjunto_User():
    conjunto_prom = set ()
    with open("User.txt","r") as archivo:
        for linea in archivo:
            control = linea.split("|")[0]
            nombre =  linea.split("|")[1]
            promedio = linea.split("|")[2][0:-1]
            conjunto_prom.add((control,nombre,promedio))
    return conjunto_prom

def Autentificar(user,passw):
    estudiante = crear_Conjunto_est()
    userdatos = crear_Conjunto_User()
    crtl=""
    for datosEst in estudiante:
        if user==datosEst[1]:
            crtl = datosEst[0]
    
    if crtl!="":     
        for datosUser in userdatos:
            if datosUser[0]==crtl:
                print(f"{crtl}:{datosUser}={passw}")
                if datosUser[1]==passw:
                    return  {
                                "Bandera": True,
                                "Usuario": user,
                                "Mensaje": "Bienvenido al Sistema de Autenticación de usuarios"
                            }
                else:
                    return  {
                                "Bandera": False,
                                "Usuario": user,
                                "Mensaje": "Contraseña incorrecta"
                            }
    else:
         return {
                    "Bandera": False,
                    "Usuario": "",
                    "Mensaje": "No existe Usuario"
                }

print("//////////////////////////////////////////////////////////")  
print(Autentificar("Alvarez Flores Hector","51AZSc0dx"))

#51AZSc0dx@  Alvarez Flores Hector