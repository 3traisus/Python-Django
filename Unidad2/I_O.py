'''
Tema: Entrada y Salida
Fecha: 11 de septiembre del 2023
Autor: Jesus Eduardo Nuñez Ramirez
'''

# Python soporta múltiples formas de formatear una cadena de caracteres. A continuación se describen:
# 1. Formateo %. operador de interpolación
# 2. format(). devuelve una versión formateada de una cadena de caracteres, usando substituciones desde argumentos
# 3. formateo avanzado. Este método soporta muchas técnicas de formateo
# 4. formateo por tipo


# 1. Formateo %. operador de interpolación

operacion = "Potencia"
numero = 100
resultado = numero**2
print("La operacion de %s  del numero %d es %f "%(operacion, numero,resultado))

# Mostrar el valor de num en octal y hexadeciaml

print("La numero %d en octal es %o y ne hexa es %x" %(numero,numero,numero))

# formato con salida %.2  (DOS decimales)

print("La operacion de %s del numero %d es %.2f"%(operacion,numero,resultado))


#    Con esta sintaxis hay que determinar el tipo del objeto:

#    %c = str, simple carácter.
#    %s = str, cadena de carácter.
#    %d = int, enteros.
#    %f = float, coma flotante.
#    %o = octal.
#    %x = hexadecimal.
estudiante = {
    "Control": 1000,
    "Nombre": "Juan Enrique Lopez Tello",
    "sexo": "M",
    "Materias":[
        {"Clave":100,"Nombre":"Base de Datos","Promedio":89.8 },
        {"Clave":200,"Nombre":"Programación","Promedio":80.7 }
    ],
    "Altura": 1.72,
}
# Imprimir Control, Nombre y Altura

print("Control: %d pertece al estudiante %s y mide %.2f"%(estudiante['Control'],estudiante['Nombre'],estudiante['Altura']))

# Imprimir Nombre y promedio 1 materia

print("Nombre de la materia: %s y el promedio es: %.2f" %(estudiante['Materias'][0]['Nombre'],estudiante['Materias'][0]['Promedio']))

# 2. format(). devuelve una versión formateada de una cadena de caracteres,
#     usando substituciones desde argumentos



carrito = {
    "id_producto": 100,
    "nombre": "Monitor Samsung de 27' ",
    "cantidad": 1,
    "precio": 5589.68,
    "descuento": 15,
    "subtotal": 5589.68,
    "datos-producto":{
        "serie": "2022ABCITJ123",
        "produccion": "Lote A-2022",
        "ano_produccion": 2022,
        "garantia": False,
    }
}
# Imprimir el nombre y numero de serie

print("Nombre del producto: {}  tiene numero de serie: {}".format(*args:"Hola"))

# 3. formateo avanzado. Este método soporta muchas técnicas de formateo
#    A) Alinear una cadena de caracteres a la derecha en 30 caracteres (>)

print("{:>30}".format("ESta es una cadena"))

#    B) Alinear una cadena de caracteres a la izquierda en 30 caracteres
#        (crea espacios a la derecha), con la siguiente sentencia

print("{:30}".format("ESta es una cadena"))

#    C) Alinear una cadena de caracteres al centro en 80 caracteres. (^)

print("{:^80}".format("ESta es una cadena"))

#    D) Truncamiento a 9 caracteres.

print("{:.9}".format("Hola mundo Hola mundo"))


# 4. Formateo por tipo
#    s para cadenas de caracteres (tipo str).
#    d para números enteros (tipo int).
#    f para números de coma flotante (tipo float).

# Formateo de numeros enteros rellenados con espacios

print("{:8d}".format(10))
print("{:8d}".format(100))
print("{:8d}".format(1000))


# Formateo de numeros rellenados con ceros

print("{:08d}".format(10))
print("{:08d}".format(100))
print("{:08d}".format(1000))
# Formateo de números flotantes, rellenados con espacios
pi = 3.1416
print("{:08f}".format(pi))
print("{:20.2f}".format(pi))
