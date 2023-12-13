
def Suma (n1,n2):
    n1 = n1 + n2
    return n1

def Resta (n1,n2):
    n1 = n1 - n2
    return n1

def Multi (n1,n2):
    n1 = n1 * n2
    return n1

def Div (n1,n2):
    n1 = n1 / n2
    return n1

def Pot (n1,n2):
    n1 = n1 ** n2
    return n1

def Residuo (n1,n2):
    n1 = n1 % n2
    return n1

def Cadena (cad):
    dato = input(cad).replace(" ","")
    return dato

def EntradasNC(cad):
    dato = input(cad)
    if dato.isdecimal:
        print("float")
    return dato

print("La suma es:",Suma(3,3))
print(Resta(3,3))
print(Multi(3,3))
print(Div(3,3))
print(Pot(2,4))
print(Residuo(7,3))
print(Cadena("Dame el nombre del personaje:"))
print(EntradasNC("Dame un numero"))

