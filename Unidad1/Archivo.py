i = 0

with open("archivo.txt", 'r') as archivo:
    lineas = archivo.readlines()

    while i < len(lineas):
        print(lineas[i], end="")
        i = i + 1