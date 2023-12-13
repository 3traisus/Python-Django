'''
Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas
con la siguiente forma:
(nombre, clave, destino)
Ejemplo:
pasajeros =    [("Felipe Gonzalez", 202101, "Guadalajara"),
                ("Gualupe Salazar", 202110, "Zamora"),
                ("Ernesto Sotomayor", 202108, "Guadalajara"),
                ("Nulvy Martinez", 202106, "León"),
                ("Jose Luis Bustamante", 202109, "Los Reyes"),
                ("Karina Tello", 202107, "Zamora"),
               ]

Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el estado al que pertencen.
Ejemplo:
ciudades = [("Guadalajara","Jalisco"),
            ("Zamora","Michoacan"),
            ("León","Guanajuato"),
           ]

Hacer un menú interactivo que permita al usuario realizar las siguientes operaciones:
- Agregar pasajeros a la lista de pasajeros
- Agregar ciudades a la lista de ciudades
- Dada la CLAVE de un pasajero, ver a que ciudad viaja
- Dada la CIUDAD, mostrar la cantidad de pasajeros que viajan a esa ciudad
- Dada la CLAVE de un pasajero, ver a que ESTADO viaja
- Dado un Estado, mostrar cuantos pasajeros viajan a ese Estado
- Salir del programa

NOTA: Haga uso de funciones
'''

pasajeros =    [("Felipe Gonzalez", 202101, "Guadalajara"),
                ("Gualupe Salazar", 202110, "Zamora"),
                ("Ernesto Sotomayor", 202108, "Guadalajara"),
                ("Nulvy Martinez", 202106, "León"),
                ("Jose Luis Bustamante", 202109, "Los Reyes"),
                ("Karina Tello", 202107, "Zamora"),
               ]

ciudades = [("Guadalajara","Jalisco"),
            ("Zamora","Michoacan"),
            ("León","Guanajuato"),
           ]

def Menu():
    op=0
    while(op!=6):
        print("////////////////////////MENU////////////////////")
        print("1.-Agregar Pasajero")
        print("2.-Agregar ciudades")
        print("3.-Dada la CLAVE de un pasajero, ver a que ciudad viaja")
        print("4.-Numero de pasajeros a un destino")
        print("5.-Busqueda de Estado de destino")
        print("6.-Salir")
        op = int(input("dame la opcion que deseas"))
        if op == 1 :
            Agregar_pasajero()
            print(pasajeros)
        elif op ==2:
            Agregar_Ciudad()
            print(ciudades)
        if op == 3 :
            Destiono_Ciudad()
        elif op == 4:
            Num_pasajeros()
        if op == 5 :
            Destiono_Estado()
        
def Agregar_pasajero():
    nombre=input("Dame el nombre:")
    clave=input("Dame la clave:")
    destino=input("Dame el destino:")
    pasajeros.append((nombre,clave,destino))
    
    
def Agregar_Ciudad():
    ciudad=input("Dame el ciudad:")
    est=input("Dame la estado:")
    ciudades.append((ciudad,est))
    
def Destiono_Ciudad():
    clave = int(input("Dame la clave del pasajero:"))
    for pasajero in pasajeros:
        if pasajero[1]==clave:
            print(f"La ciudad Destino es {pasajero[2]}")
            break

def Destiono_Estado():
    clave = int(input("Dame la clave del pasajero:"))
    for pasajero in pasajeros:
        if pasajero[1]== clave:
            for ciu in ciudades:
                if pasajero[2] == ciu[0]:
                    print(f"El estado Destino es:{ciu[1]}")
                    break
    
def Num_pasajeros():
    cont = 0
    desti = input("Dame el destino:")
    for destino in pasajeros:
        if desti == destino[2] or desti == destino[2]:
            cont=cont+1
    print(f"El numero de pasajeros es igual: {cont}")
            

Menu()