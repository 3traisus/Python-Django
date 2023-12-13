import Recursos.Listas_Tuplas_Conjuntos_Dicc as rsLTC


dic = rsLTC.New_diccionario(["Saludos","Despedida"],["Hola","Adios"])

print(dic)

#Agregando Elementos 
dic["Nuevo"]="Elemento"
print(dic)

#Uniendo Dic
dic.update(rsLTC.New_diccionario(["Variables","Constante"],["X","Y"]))
print(dic)

#Borrando los datos
#dic.clear()

#Borrando Elementos
#dic.pop("Constante")
dic.popitem()
dic.popitem()
c,v = dic.popitem()
print(dic)


lista = [e for e in range(1,11)]
lista2 = lista[1:10]
print(lista,lista2)

Grupo = []
estudiantes = rsLTC.New_diccionario(["Materias","Promedio","ActExtra"],
                [["Matematicas","Español","Programacion"],["90","75","100"],["Ajedrez","Futbol"]])
print (estudiantes)


