'''
Tema: Gestión de excepciones
Fecha: 22 de septiembre del 2022
Autor: Leonardo Martínez González
'''

#    En algunas ocasiones nuestros programas pueden fallar ocasionando su detención.
#    Ya sea por errores de sintaxis o de lógica, tenemos que que ser capaces de detectar esos
#    momentos y tratarlos debidamente para prevenirlos.

#    Los errores detienen la ejecución del programa y tienen varias causas. Para poder estudiarlos
#    vamos a provocar algunos intencionadamente.
#    Tipos: Errores de sintaxis, de nombre y semánticos.

# 1. Excepciones: Las excepciones son bloques de código que nos permiten continuar
#    con la ejecución de un programa pese a que ocurra un error.

#    Se trata de una forma de controlar el comportamiento de un programa
#    cuando se produce un error.

# 2. Sintaxis:
'''
    try:
        # Intenta ejecutar la instrucion(es)
    except:
        # Si ocurre un error aqui se trata
    else:
        # Si entra al bloque try se ejecuta este bloque de código
    finally: 
        # Siempre se ejecutara este código
'''

# Los ejemplos más comunes que podemos nombrar de excepciones:
#
# 1. Tratar de convertir a entero un string que no contiene valores numéricos. (ValueError)
# 2. Tratar de dividir por cero.
# 3. Abrir un archivo de texto inexistente o que se encuentra bloqueado por otra aplicación.
# 4. Conectar con un servidor de bases de datos que no se encuentra activo.
# 5. Acceder a subíndices de listas o tuplas inexistentes.

'''
# Ejemplo 1: Calcular si un  numero es PAR o IMPAR, introducir el dato desde teclado 
# (ValueError)
'''
# try:
#     numero = int(input("Dame un Numero:"))
#     if numero % 2 ==0:
#         print("El numero es par")
#     else:
#         print("El numero es impar")
# except ValueError:
#     print("Solo se permite numeros")


'''
# 2. Tratar de dividir por cero. (ZeroDivisionError)
ValueError
'''

resultado = -1
try:
    numero = 100
    resultado = numero / 0
except ZeroDivisionError:
    print("Division entre 0")
finally:
    print(resultado)

'''
# 3. Abrir un archivo de texto inexistente.
#    (FileNotFoundError)
'''

def abrir_archivo(archivo):
    try:
        f = open(archivo,"r")
    except FileNotFoundError:
        print("No existe el archivo")
    else:
        print(archivo, f"Tiene {len(f.readlines)}")

abrir_archivo("x.txt")

'''
# 4. Conectar con un servidor de bases de datos de MongoDB que no se encuentra activo.
#      Importar pymongo
#      pip install pymongo
'''

'''
# 5. Acceder a subíndices de listas o tuplas inexistentes. (IndexError)
'''
lista = ["José", "Ana", "Arturo", "Rocio", "Maria"]

'''
# ========== Generación manual de excepciones con la declaración raise en Python ==========
Podemos usar la declaración raise dentro de una declaración if
para generar una excepción específica si ocurre una condición específica. 
'''

'''
#1. Generar una excepción ZeroDivisionError
'''



'''
# 2. Generar una excepción TypeError si var no es una variable de tipo entero.
'''



'''
# 3. Generar una excepción ValueError si month es mayor que 12
'''


'''
# ERRORES PERSONALIZADOS CON assert
'''


'''
# PROPAGACIÓN DEL ERROR con raise
'''
