#coding: utf8
#Autor: Pol Balada
#22/2/18

#Fem que importi les comandes de LINUX i llençem la comanda clear perque el codi surti al inici del tot
import os
os.system("clear")

#Fem que importi el numero pi per a facilitar els calculs de cicumferencia
from math import pi

titulo="CALCULADORA DE AREAS"
print titulo.center(75, "=")

figura=raw_input("Que figura quieres calcular (T/C)? ")

if(figura=="T") or (figura=="t") :
    base=input ("Introduzca la Base: ")
    altura=input ("Introduzca la Altura: ")
    
    if(base<0) or (altura<0) :
        print "ERROR, las medidas negativas no existen"
    else :
        area=(base*altura)/2
        print "L'area es igual a ", area
elif(figura=="C")or(figura=="c") :
    radi=input ("Introdueix el radi: ")
    
    if (radi<0) :
        print "ERROR, las medidas negativas no existen"
    else :
        print "L'area es igual a ", round (pi*radi**2,2)
else :
    print "ERROR, no es una figura valida"
