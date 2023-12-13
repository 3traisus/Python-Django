import Listas_Tuplas_Conjuntos_Dicc as ltc


#metodo que extrae los datos de un archivo txt no json, apartir de un seperador 
def Extraer_datos_txt(url_archivo,separador):
    listdatos = []
    with open(url_archivo,"r") as archivo:
        for linea in archivo:
            temp = linea.split(r"|") 
            listdatos.append[temp]
            
    