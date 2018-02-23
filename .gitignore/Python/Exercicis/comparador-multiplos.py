#coding: utf8
#Autor: Pol Balada
#23/2/18

#Fem que importi les comandes de LINUX i llençem la comanda clear perque el codi surti al inici del tot
import os
os.system("clear")

print """
COMPARADOR DE MULTIPLOS
"""

num1=input ("Introdueix el primer numero: ")
num2=input ("Introdueix el segon numero: ")

if (num1==0) or (num2==0) :
    print "Error, no es pot fer amb zero"
elif (num1==num2) :
    print "Els dos numeros son iguals, ", num1, "es multiple de ", num2
else :
    if (num1>num2) :
        mayor=num1
        menor=num2
    else :
        mayor=num2
        menor=num1
    
    if (mayor%menor==0) :
        print mayor , " es multiple de ", menor
    else :
        print mayor , " no es multiple de ", menor
