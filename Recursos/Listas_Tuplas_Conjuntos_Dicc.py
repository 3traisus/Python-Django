import json
#Creacion de Lista 
def New_lista(*elementos):
    if len(elementos)!=0:
        if elementos[0]!="":
            lista = list(elementos)
        else:
            lista =[]
    else:
        lista =[]
    return lista

#Creacion de tupla 
def New_tupla(*elementos):
    tupla = elementos
    return tupla

#Creacion de Conjunto 
def New_conjunto(*iterable):
    return set(iterable)

#Creacion de Diccionario 
def New_diccionario(claves,valor):
    dic = dict.fromkeys(claves)
    if len(valor)>0:
        for clav in enumerate(claves):
            dic[clav[1]] = valor[clav[0]]
    return dic

#Creacion de lista de Diccionario 
def Lista_diccionario(claves,valor,div,*ele):
    lista = New_lista(*ele)
    dic = dict.fromkeys(claves[0:div])
    if len(valor)>0:
        for clav in enumerate(claves[0:div]):
            dic[clav[1]] = valor[clav[0]]
        lista.append(dic)
    if len(claves) > len(lista):
        return Lista_diccionario(claves[div:],valor[div:],div,*lista)
    return lista

#Cracion de una lista de diccionario apartir 
def Lista_dic(claves,Listavalores):
    dic = dict.fromkeys(claves)
    lista = []
    for ind,linea in enumerate(Listavalores):
        for pos,datos in enumerate(Listavalores[ind]):
            dic[claves[pos]] = datos
        lista.append(dic)
    return lista
        
#Crea una tupla de listas apartir de un diccionario 
def TupladeListas_diccionario(diccionario):
    listClv = []
    listVal = []
    for dic in diccionario.items():
        listClv.append(dic[0])
        listVal.append(dic[1])
    return listClv,listVal

#Crear una lista de conjuntos apartir de de un diccionario
def Multiconjunto_diccionario(diccionario):
    multi = []
    for dic in diccionario.items():
        multi.append(New_conjunto(*dic))#*dic manda los elementos de una tupla uno x uno
    return multi

#print(New_lista(*("Hola","Adios"),*["A","B"],*{"X","Y"}))
#print(TupladeListas_diccionario({"Name":"Hola","Apellido":"Adios"}))
#print(TupladeListas_diccionario({"Name":"Hola","Apellido":"Adios"})[0])
#print(Multiconjunto_diccionario({"Name":"Hola","Apellido":"Adios"}))
#print(New_diccionario(["Saludo","Despedida"],["Hola","Adios"]))

#print(Lista_diccionario(["NOMBRE","APELLIDO","NOMBRE","APELLIDO"],["JESUS","NUÑEZ","CECI","LOPEZ"],2,))

