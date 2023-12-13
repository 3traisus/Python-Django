
#Creacion de Lista 
def New_lista(*elementos):
    lista = list(elementos)
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