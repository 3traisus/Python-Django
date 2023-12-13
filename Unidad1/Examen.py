'''
cantidad_minutos = int(input("Dame la cantidad de minutos: "))
horas = cantidad_minutos / 60
minutos = cantidad_minutos % 60
print("Las horas y minutos son: ", int(horas),"hrs",minutos,"min")

Programa que lea una cadena por teclado y comprobar si existeuna letra mayúscula

cadena = input("Dame una cadena: ")
for mayus in cadena:
    if mayus.isupper():
        print("La cadena contiene letras mayusculas")
        break
    else:
        pass

Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.(la tabla debe de ir desde el 1 hasta 110).
'''

cont = 0
for x in range(1,6):
    for y in range(1,11):
        print(f"{x} x {y} = {x*y}")
        
    
#Ejercicio 2
'''
sueldo_Base= float(input("Dame el sueldo base:"))
porcenaje_Venta=10
venta =0
for x in range (1,4):
    venta+= float(input(f"Venta {x} Total:"))
comision = venta * porcenaje_Venta/100
sueldo_Total = comision + sueldo_Base
print(f"Comision por venta:{comision} \n Sueldo Total:{sueldo_Total}")'''


#Ejercicio 3

cal_par=0
for x in range (1,4):
    cal_par+= float(input(f"Calificacion parcial {x}:"))
cal_par = cal_par * .55 / 3
examen = float(input(f"Calificacion Examen:")) * .3
trab_fin = float(input(f"Calificacion trabajo Final:")) * .15
total = cal_par +trab_fin + examen
print(f"Calificiacion_Parcial:{cal_par},Examen:{examen},TrabajoFinal:{trab_fin},Total={total}")

