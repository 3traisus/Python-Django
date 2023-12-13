"""
Tema: Listas
Fecha: 28 de agosto del 2023
Autor: Leonardo Martínez González
"""

'''
Una lista en Python es:

1. Ordenada: esto quiere decir que los elementos dentro de ella están indexados y
   se accede a ellos a través de una locación indexada. 

2. Editable: los elementos dentro de una lista pueden editarse, añadir nuevos o eliminar los que ya tiene. 

3. Dinámica: las listas pueden contener diferentes tipos de datos y hasta de objetos.
   Esto significa que pueden soportar paquetes multidimensionales de datos, como un array o muchos objetos. 

4. No única: esencialmente, esto quiere decir que la lista puede contener elementos duplicados
   sin que arroje un error. 

Si te has familiarizado con la programación, podría parecer que la lista en Python es similar a un array
en otros lenguajes. Seamos claros al respecto: son muy distintos entre ellos.
Python tiene un tipo de datos array nativo por esa misma razón.

Referencia: https://blog.hubspot.es/website/lista-python#:~:text=Python%20tiene%20cuatro%20tipos%20de,a%20funci%C3%B3n%2C%20desempe%C3%B1o%20y%20maleabilidad.

'''
# 1. Crear una lista. con corchetes o con el contructor list()
# lista_nombres = ['Juan', 'Pedro', 'Carlos', 'José', 'Nohemi', 'Luisa','Ana María','Nulvy','Antonio','Zulma']
# lista_numeros = list('0123456789')

# Para accesar a cada elemento es por su índice

# Para accesar al último elelemento es con el índice -1, penúltimo -2, . . . hasta llegar al primero -10.
# Para el caso de que la lista contenga 10 elementos.

# Obtención de rangos de elementos (rebanadas), siempre comienza por la izquierda

# Agregar elementos a la lista con el método append()

# Insertar elementos en cualquier posición en la lista con el método insert(index, elemento)

# Sacar un elemento de la lista de acuerdo al indice especificado con el método pop(index)

# Insertar listas dentro de otras listas

# Concatena los elementos de dos listas

# Con el método sorted() o ()) de la lista, se ordena la lista, si se incluye el parámetro reverse=True, se ordena a la inversa

# lista_ordenada = sorted(lista_nombres, key= llave, función o campo , reverse=True)

'''
Otros metodos
.clear(): elimina todos los elementos de la lista.
.copy(): arroja una copia de la lista.
.count(): arroja el número de elementos con el valor indicado.
.extend(): añade los elementos de una lista (o cualquier iterador) al final de la lista actual.
.insert(): añade un elemento en la posición que se indica.
.pop(): elimina el elemento de la posición que se indica.
.reverse(): invierte el orden de la lista. 
'''

'''
Práctica de listas
1. Leer un archivo de texto, cada linea representa los datos de UN estudiante, genere una lista de listas, donde
cada lista son los datos de un estudiante, ésta lista insertela en otra lista (grupo).


2. Muestre los estudiante ordenados alfabeticamente

3. Cree otro archivo de texto, agregue una contraseña de tamaño 12 para cada estudiante,
guardelas en texto plano y encriptada.
'''
import random as rar
import encodings as ec
import re 
#import bcrypt as cryp
'''
i = 0
lista_nombres=[]
lista_grupo=["Jonathan Francisco","Fercho Aguilera","Isagod Alvarado","Manzoscout Diaz","Abel Arceo"]

with open("nombres.txt", 'r') as archivo:
    lineas = archivo.readlines()

    while i < len(lineas):
      name,vacio=lineas[i].split('\n')
      lista_nombres.append(name.replace(" ",""))
      i = i + 1
      
lista_grupo.extend(lista_nombres)
print(lista_grupo)

def Password(tam):
   minus=["a","b","c","d","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
   mayus=["A","B","C","D","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
   carac =["@","!","?","%","&","$"]
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
   if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%?&])',pas):
      return pas
   else:
      Password(tam)



def hash_password_bcrypt(password):
    salt = cryp.gensalt()
    hashed = cryp.hashpw(password.encode('utf-8'), salt)
    return hashed'''

#print(hash_password_bcrypt(Password(12)))
#print(Password(12))

cad = "1aA@1"
if re.match(r'(?=.*[a-z])(?=.*[A-Z])(?=.\D*\d{2})(?=.*[@$!%?&])',cad):
   print ("Correcto")
else:
   print("Incorrecto")


