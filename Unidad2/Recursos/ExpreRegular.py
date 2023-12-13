import re as re


def GenExpRegulares(tipo, cantidad,*carac):
    '''En Tipo se abarcara Numeros,Minisculas,Mayusculas,Especiales,
    
    Notas: Recuerda Siempre Dejar lugar la posicion 0 para condiciones de Inicio,1 para condiciones Generales, 2 para Fin de cadenas;
                En caso de no llevarlas poner null en su tipo, y 0 en cantidad;
                
            Condidicion General:solo existe condiciones de tener algun numero de elementos que no sean en grupos    
                por ejemeplo tener 3 numeros o tener un @ en cualquier parte de la cadena
             
            En tipo tendra que ir siempre "Ins:"antes de usar N(numeros), m(Minusculas),M(Mayusculas),E(Especiales)
            en caso de usar una cadena sera #cadena y con caracteres tendra que ser (#,$,etc), 
            siempre poner primero Numeros,minuscular,Mayusculas,Especiales luego los caracteres y por ultimo cadenas
            
            
            Si usas Especiales tendras que poner un iterable mas con los Caracteres de lo contrario es innecesario
            en Tipo tambien puedes usar caracteres especificos que quieras usar ademas de poder usar cadenas completas 
            ejemplo@gmail.com Tipo=[Minusculas_Caracter_Cadena]
            Por ultimo para combinar se representara de esta manera N:numeros, m:minusculas, M:Mayusculas, E:especiales
            para caracteres y cadenas sera de la siguiente forma ("#","@","$"):caracteres y #Cadena 
            Siempre dejando caracteres en penultimo lugar y cadena de ultima
            Ejemplo: Tipo=NmME(@)#Hola, Cantidad=2, Caracteres=#$% -> en esa posicion debe haber 2 elementos ya sean:
                Numeros,Minisculas,Mayusculas,Especiales | @@ | HolaHola 
            
    '''
    num=r"[\d]"
    min=r"[a-z]"
    may=r"[A-Z]"
    esp= f"[{ExtraerCarac(carac)}]"
    esp_usable = r""+esp
    exp_reg =""
    ind = -2
    #print(esp_usable)
    #x=r"^(?:\D*\d){5}\D*$"
    #formCant0=r"(?=.*\d{5})"
    if len(tipo) == len(cantidad):
        for pos,valores in enumerate(zip(tipo,cantidad)):
            #print(valores)
            if(pos==0):
                exp_reg = exp_reg+r"^("
                print (type(valores[1]))
                if str(type(valores[1])).find("int")!=-1:
                    for car in enumerate(valores[0][4:]):
                        #print(f"{ind}<{car[0]}")
                        if ind <= car[0]:
                            if car[0] != 0:
                                exp_reg = exp_reg+r"|"
                            if car[1] == "N":
                                exp_reg = exp_reg + num
                                #exp_reg = exp_reg + num + r"{"+f"{valores[1]}"+r"}"
                            elif car[1] == "m":
                                exp_reg = exp_reg + min 
                            elif car[1] == "M":
                                exp_reg = exp_reg + may 
                            elif car[1] == "E":
                                exp_reg = exp_reg + esp 
                            elif car[1] == "[":
                                cad=""
                                ind = str (valores[0][car[0]+4:]).find("#")
                                print(f"{valores[0][car[0]+4:]}")
                                print(f"{valores[0][car[0]+4:ind+4]}/{ind}/{car[0]}")
                                if  ind !=-1:#Tienes Error:Recorta mal la cadena
                                    cad = cad+str(valores[0][car[0]+4:ind+4]).replace(",","")
                                    exp_reg = exp_reg + cad
                                else:
                                    cad = cad+str(valores[0][car[0]+4:-1]).replace(",","")
                                    cad = cad+"]"
                                    exp_reg = exp_reg + cad
                                    exp_reg = exp_reg+r"){"+f"{valores[1]}"+r"}"
                                    break
                            elif car[1] == "#":
                                exp_reg = exp_reg + valores[0][car[0]+5:]
                                exp_reg = exp_reg+r"){"+f"{valores[1]}"+r"}"
                                break
                    else: 
                        exp_reg = exp_reg+r"){"+f"{valores[1]}"+r"}"
                else:
                    tupla_valor = list(valores[1])#convierte en lista la tupla de valores Recibidos anteriormente de valores en su posicion 1
                    sum = str(valores[0][4:]).count("N") + str(valores[0][4:]).count("m") + str(valores[0][4:]).count("M") + str(valores[0][4:]).count("(") + str(valores[0][4:]).count("#")#Suma los caracteres identificadores para saber cuantos elementos le faltan o le sobran a la lista nueva
                    tamaño = len(tupla_valor) #determinamos el tamaño de la lista
                    if sum < tamaño:   
                        for x in range(tamaño-sum):
                            tupla_valor.pop()#eleminamos elementos extra de la lista                    
                    elif sum > tamaño:
                         for x in range(sum-tamaño):
                            tupla_valor.append(tupla_valor[tamaño-1])#agregamos elementos extra a la lista
                    
                    for x,tupval in enumerate(zip(valores[0][4:],tupla_valor)):#x contiene el indice y tupval una tupla con valores y cantidades
                        if ind <= x:
                            if x != 0:
                                exp_reg = exp_reg+r"|"
                            if tupval[0] == "N":
                                exp_reg = exp_reg + num + r"{"+f"{tupval[1]}"+r"}"
                            elif tupval[0] == "m":
                                exp_reg = exp_reg + min + r"{"+f"{tupval[1]}"+r"}"
                            elif tupval[0] == "M":
                                exp_reg = exp_reg + may + r"{"+f"{tupval[1]}"+r"}"
                            elif tupval[0] == "E":
                                exp_reg = exp_reg + esp + r"{"+f"{tupval[1]}"+r"}"
                            elif tupval[0] == "[":
                                print("XD")
                                cad=""
                                ind = str (tupval[0][x+4:]).find("#")
                                #print(f"{car[0]+4}/{ind}")
                                if  ind !=-1:
                                    cad = cad+str(valores[0][x+4:ind+4]).replace(",","")
                                    exp_reg = exp_reg + cad + r"{"+f"{tupval[1]}"+r"}"
                                else:
                                    #print("XD")
                                    cad = cad+str(valores[0][x+4:-1]).replace(",","")
                                    cad = cad+"]"
                                    exp_reg = exp_reg + cad
                                    exp_reg = exp_reg+ r"{"+f"{tupval[1]}"+r"})"
                                    break
                            elif tupval[0] == "#":
                                print("XDD")
                                exp_reg = exp_reg + valores[0][x+5:]
                                exp_reg = exp_reg + r"{"+f"{tupval[1]}"+r"})"
                                break
                    else: 
                        exp_reg = exp_reg+ r")"
                        
                        
                
    return exp_reg
        


def ExtraerCarac(carac):
    cad=""
    for x in carac:
        if cad.find(x)==-1:
            cad=cad+f"{x}"
    return cad


#Nos falta evaluar que no vengas dobles caracteres o dobles cadenas
exp=GenExpRegulares(["Ins:NmM[@,$]"],[2],"#","#","%","&")
print(exp)

cad ="AAAB2"
if re.match(exp,cad):
    print("Correcto")
else:
    print("Incorrecto")