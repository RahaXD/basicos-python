print("-------------------------------------------------------")
print("Ejercicio1: OPERACIONES ARITMETICAS.")
print("-------------------------------------------------------")

print("INGRESE 2 NUMEROS PARAR LAS OPERACIONES ARITMETICAS")

n1 = float( input("n1: ") )
n2 = float( input("n2: ") )
print(n1, " + " , n2," = ", n1+n2)
print(n1, " - " , n2," = ", n1-n2)
print(n1, " * " , n2," = ", n1+n2)
print(n1, " / " , n2," = ", n1/n2)
print(n1, " % " , n2," = ", n1%n2)

print("-------------------------------------------------------")
print("Ejercicio2: JUEGO CON NUMEROS RAMDOMICOS.")
print("-------------------------------------------------------")
print("adivina el numero secreto")

import random
comienza = random.randint(1, 3)
print(comienza)
for i in range(2):
    n1= input()
    if comienza == n1:
        print('ganaste')
    else:
        print('intento ', i+1 ,' fallido')
        if i == 3 :
            print(comienza)

print("-------------------------------------------------------")
print("Ejercicio3: numero primo.")
print("-------------------------------------------------------")

print("¿Qué número quieres saber si es primo?")
numero= int(input(" n= "))
valor= range(2,numero)
contador = 0
for n in valor:
  if numero % n == 0:
    contador +=1
    print("divisor:", n)
 
if contador > 0 :
  print(" no es primo" )
else:
  print("El nÚmero es primo")
  
print("-------------------------------------------------------")
print("Ejercicio 4: ciclos.")
print("-------------------------------------------------------")

print("EDADES")
print ("CICLO FOR")
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, inicio="\t")
    print("")
print ("INVERCION")
amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))
print("CICLO WHILE")
dia = 0    
semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
while dia < 7:
   print("Hoy es " + semana[dia])
   dia += 1
   
print("-------------------------------------------------------")
print("Ejercicio 5: EDADES.")
print("-------------------------------------------------------")

print ("¿Cuántos años tienes?")
edad = int(input("edad = "))
for i in range(edad):
    print("Has cumplido " + str(i+1) + " años")
print("vas a cumplir", edad+1)

print("-------------------------------------------------------")
print("Ejercicio 6: MASAS CORPORAL.")
print("-------------------------------------------------------")

n = input("Su nombre por favor: ")
e = int(input("Su edad en años por favor: "))
a = float(input ("Su altura en metros por favor: "))
est = a
m = float (input("Su masa en kilogramos por favor :"))
IMC = m / est**2
if(e < 18):
    print("Usted es menor de edad")
else:
    print("Usted es mayor de edad")
print("IMC: " + str(IMC) )

if IMC >= 0 and IMC <= 15.99 :
    print ("Delgadez severa")
elif IMC >= 16.00 and IMC <= 16.99 :
    print ("Delgadez moderada")
elif IMC >= 17.00 and IMC <= 18.49:
    print ("Delgadez leve")
elif IMC >= 18.50 and IMC <= 24.99 :
    print ("Normal")
elif IMC >= 25.00 and IMC <= 29.99:
    print ("Sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99:
    print ("obesidad leve")
elif IMC >= 35.00 and IMC <= 39.00:
    print ("obesidad media")
elif IMC >= 40.00:
    print ("obesidad morbida")