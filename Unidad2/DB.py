'''
Tema: Funciones
Fecha: 12 de septiembre del 2023
Autor: David Junior Rodriguez Farias
Link: https://www.youtube.com/watch?v=_nAuo8JsAcM  *args y **kwargs
Link: https://www.youtube.com/watch?v=8JpE9CwfOJc funciones lambda
'''
import mysql
import mysql.connector
import json 
'''
1. Funciones con paso de Parámetros por valor o referencia 
2. Funciones con argumentos con valor por defecto
3. Funciones que retornan varios valores
4. Funciones lambda
5. Funciones con argumentos arbitrarios. Se utiliza cuando no sabemos la cantidad
   de argumentos que vamos a recibir
'''

'''
 1. Funciones con paso de Parámetros por valor o referencia
    Dependiendo del tipo de dato que enviemos a la función,
    podemos diferenciar dos comportamientos:

    Paso por valor: Se crea una copia local de la variable dentro de la función.
    Paso por referencia: Se maneja directamente la variable, los cambios realizados
    dentro de la función le afectarán también fuera.

    Tradicionalmente:
    Los tipos simples se pasan por valor: Enteros, flotantes, cadenas, lógicos...
    Los tipos compuestos se pasan por referencia: Listas, diccionarios, conjuntos...
'''
# Crear una función que doble el valor de un número
def doblar_valor(numero):
    numero *=2
    return numero
n = 10
print("n:",n, "El doble de n es: ",doblar_valor(n))

# Crear funciones con paso de parámetros por referencia
# Crear una funcion que reciba una lista y la ordene
lista = ["Juan", "Pedro", "Luis", "Karmina", "Leticia", "Armando"]

def ordenar_lista(mi_lista):
    mi_lista.sort()

print(lista)
ordenar_lista(lista)
print(lista)

'''
2. Funciones con argumentos con valor por defecto
   Tal vez queramos tener una función con algún parámetro opcional,
   que pueda ser usado o no dependiendo de diferentes circunstancias.
   Para ello, lo que podemos hacer es asignar un valor por defecto a la función.
'''
# Crear una función que se conecte a una Base de Datos de MySQL Server
# https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=81&codigo=81&inicio=75
# pip install mysql-connector

def conectar_mysql(host="localhost",user="root",pwd="",bd="videogames"):
    try:
        conexion = mysql.connector.connect(host=host,user=user,password=pwd,database=bd)
        return conexion
    except Exception as error:
        return  error

print(conectar_mysql('www.google.com'))
# Crear una función que reciba la conexion a la Base de Datos y una consulta SQL
# Retorne en formato JSON el resultado de la consulta

def consulta_sql(conn,sql):
    lista = []
    try:
        #Crear el cursor
        mi_cursor = conn.cursor()
        mi_cursor.execute(sql) #consulta valida
    except mysql.connector.errors.ProgrammingError as e:
        print(e)
    except Exception as error:
        print(error)
    else:
        for reg in mi_cursor:
            lista.append(
                            {
                                "Codigo":reg[0],
                                "Nombre": reg[3],
                                "Precio": reg[4]
                            }
                        )
        mi_cursor.close()
    conn.close()
    return json.dumps(lista)
    
mi_conexion = conectar_mysql()
consulta_sql (mi_conexion,sql="Select * from Empleados")

'''
[
    {
        "Codigo":200
        "Nombre": "Consola Videojuegos XXX"
        "Precio": 356.90
    }
]'''

# 3. Funciones que retornan varios valores
#    Crear una función que reciba una cantidada entera de segundos,
#    la función debe regresar las horas, minutos y los segundo


# Crear una función que sume dos valores, regresar la suma de y los valores que esta recibiendo
def sumar(a,b):
    return a+b,a,b

x,y,z = sumar(10,5)
print(x,y,z)

# Crear una funcion que reciba un numero en segundos y que regrese: h, m, s

def tiempo(cant):
    horas = cant / 3600
    minutos = int((cant % 3600)/60)
    seg =  int((cant % 3600)%60)
    return horas,minutos,seg

horas,min,seg = tiempo(1000)
print(f"{horas}:{min}:{seg}")


# 4. Funciones lambda
'''
Funciones lambda o anónimas, son de una sola linea, solo las ocupamos una sola vez.
“Python lambdas are only a shorthand notation if you’re too lazy to define a function.”
Lo que significa algo así como, “las funciones lambda son simplemente una versión acortada,
que puedes usar si te da pereza escribir una función”

1. Definir una función lambda con un ejemplo
2. Llamada de otras funciones dentro de una función lambda
3. Ordenar una lista
3. Pasarlas como parámetros a filter y map. 
   filter filtra elementos, toma dos parámetros: (una_funcion, lista)
   map por cada elemento de la lista llama al elemento y regresa el elemento ya modificado
'''


# La función anterior expresada en función Lambda
lambda nombre: f"Hola{nombre}"


# Pero debes asignar el resultado a una variable, de lo contrario no servira de mucho

saludo = lambda nombre: f"Hola {nombre}"
print(saludo("Joel"))

def suma(a,b):
    return a+b

suma2 = lambda a,b: a+b
print(suma2(10,10))

# Si es menor de edad regresar False de lo contrario regresar la edad
listaedad = [11,12,13,18,19] 
menor_edad = lambda e:e if e < 10 else False

# Función lambda que regresa False si es menor de edad, de lo contrario regresa la edad

# Recorrer la lista para aplicar la función lambda

for e in listaedad:
    print(menor_edad(e))


# Crear una función Lambda que reciba un número y mande llamar a una función
def cuadrado (x):
    x**2
cuadradoval = lambda e:cuadrado(e) 
for e in lista:
    print(cuadradoval(e))
# la función regresará el cuadrado de ese numero
# Después, utilizando la lista de edades imprimir las edades al cuadrado



lista = [[500, "Juan José", 18, 90.8 ],
        [200, "Antonio", 28, 65.8 ],
        [100, "Zacarias", 17, 100.0 ],
        [400, "Karmina", 19, 55.8 ],
        [300, "Beatriz", 20, 87.0 ],
         ]

# Ordenar la lista e imprimirla

# Ordenar por Nombre

# Regresar los estudiantes aprobados, de lo contrario regresar un False


# 5. Funciones con argumentos arbitrarios. Se utiliza cuando no sabemos la cantidad
#    de argumentos que vamos a recibir
'''
Argumentos arbitrarios. Se utiliza cuando no sabemos la cantidad de argumentos
que vamos a recibir
'''


'''
 y keyword arguments **kwargs, es un diccionario con numero de elementos variable
'''
