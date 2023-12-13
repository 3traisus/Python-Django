
'''
Tema: conjuntos
Fecha: 06 de septiembre del 2023
Autor: Leonardo Martínez González
'''

# 1. Definición. en Python es utilizado para trabajar con conjuntos de elementos.
#    La principal característica de este tipo de datos es que es una colección cuyos elementos
#    no guardan ningún orden y que además son únicos.
#    los principales usos de esta clase se usan para conocer si un elemento pertenece o no
#    a una colección y eliminar duplicados de un tipo secuencial (list, tuple o str).

c1 = set()
c2 = {1,2,3,4}
c3  = (i for i in range(1,11,2))#Numeros pares del 0-10

# 2. Creación. Para crear un conjunto, basta con encerrar una serie de elementos entre llaves {},
#    o bien usar el constructor de la clase set() y pasarle como argumento un objeto iterable
#    (como una lista, una tupla, una cadena …).




#    Usando la función frozenset. es inmutable y su contenido no puede ser modificado
#    una vez que ha sido inicializado
c4 =  frozenset(chr (letra) for letra in range(65,91))#Caracteres mayusculas

# 3. Para acceder a los elementos de un conjunto. Dado que los conjuntos son colecciones
#    desordenadas, en ellos no se guarda la posición en la que son insertados los elementos
#    como ocurre en los tipos list o tuple. Es por ello que no se puede acceder a los elementos
#    a través de un índice.

for carac in c4:
    print(carac)

# 4. Añadir elementos: con el método add() ó con el método update()
#    Agregar el numero 8 al conjunto c


c2.add(6)
#    Agregar varios elementos al conjunto con el metodo update()

c2.update(9,8,7)
print(c2)

# 5. Eliminar elementos del conjunto: discard(elemento), remove(elemento), pop() y clear()
#    discard(elemento) y remove(elemento) son muy parecidos, solo que remove lanza una excepcion KeyError
#    en caso de no existir el elemento

c2.discard(9)
print(c2)
c2.remove(8)
print(c2)
#     pop() devuelve un elemento aleatorio y lo elimina, si el conjunto esta vacio lanza una
#     excepcion KeyError.

print(c2.pop(7))

# #    El método clear() elimina todos los elementos del conjunto

c1.clear()

#    Número de elementos en un conlunto con la función len()

print(len(c1))
# #    Verificar si un elemento esta dentro de un conjunto

print (2 in c3)

# ************************ Operaciones con conjuntos
a = set( i for i in range(0,11,2))
b = set(i for i in range(1,10,2))
print(f"{a}/{b}")
# 1. Union  ( | )

print(a|b)

# 2. Intersección ( & )

a.add(5)
print(a&b)

# 3. Diferencia ( - )

print (a-b)


# 4. Diferencia simétrica ( ^ ). es el conjunto que contiene los elementos de A y B
#    que no son comunes.

print(a^b)

# 5. Inclusión de conjuntos.  Se utiliza el operador <= para comprobar si un conjunto A
#    es subconjunto de B y el operador >= para comprobar si un conjunto A es superconjunto de B.
sub1 = set(1,2,3)
sub2 = set(1,2,3,4)
print(sub1<=sub2)

# 5. Conjuntos disjuntos. Dos conjuntos A y B son disjuntos si no tienen elementos en común,
#    es decir, la intersección de A y B es el conjunto vacío.


# 6. Igualdad de conjuntos. En Python dos conjuntos son iguales si y solo si todos los elementos
#    de un conjunto están contenidos en el otro. Esto quiere decir que cada uno es un subconjunto
#    del otro.