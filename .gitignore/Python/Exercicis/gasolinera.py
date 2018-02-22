# coding: utf8
# Autor: Pol Balada
# 21/2/18

#Fem que importi les comandes de LINUX i llençem la comanda clear perque el codi surti al inici del tot
import os
os.system("clear")

# Mostrem la llista de preus
print """
################################################
#                                              #
#          BIENVENIDO A LA GASOLINERA          #
#                                              #
################################################

¿que tipo de gasolina quiere?

 -Escriva 1 para Super: Normal (1,50€), Turbo (1,55€)
 -Escriva 2 para Sin plomo: Normal (1,60€), Con aditivo de sabor naranja (1,65€)
 -Escriva 3 para Diesel: Normal (1,70€), Fast&Fourious (1,75€)
"""

tipo_gasolina=input("Introduzca tipo de gasolina: ")

# Si escull gasolina SUPER (1) li preguntem quin tipus de SUPER
if (tipo_gasolina==1) :
    print "Ha elegido Gasolina Super"
    print """Que tipo de Gasolina super quiere?
    Escriva 1 para Normal (1,50€/l)
    Escriva 2 para Turbo (1,55€/l)"""
    tipo_super=input("Escoga tipo de Gasolina super: ")
# Preguntem el tipus de gasolina SUPER, demanem els litres que voldrà i els multipliquem per el preu, ho mostrem per pantalla
    if (tipo_super==1) :
        print "Ha escogido Gasolina Super Normal"
        litros=input("Introduzca los litros que desea comprar: ")
        if litros <=0 :
            print "Ha introducido un numero erroneo."
        else :
    	    print "Ha introducido", litros , "l, el precio es de ", litros*1.5, "$"
    elif (tipo_super==2) :
        print "Ha escogido Gasolina Super Turbo"
        litros=input("Introduzca los litros que desea comprar: ")
        if litros <=0 :
		    print "Ha introducido un numero erroneo."
        else :
            print "Ha introducido", litros , "l, el precio es de ", litros*1.55, "$"
# Si escriu un numero erroni de gasolina, enviem missatge d'error    else :
    else :
        print "Ha introducido un numero erroneo."

# Si escull gasolina SIN PLOMO (2) li preguntem quin tipus de SIN PLOMO

elif (tipo_gasolina==2) :
    print "Ha elegido Gasolina Sin Plomo"
    print """Que tipo de Gasolina Sin Plomo quiere?
    Escriva 1 para Normal (1,60€/l)
    Escriva 2 para Con aditivo de sabor naranja (1,65€/l)"""
    tipo_super=input("Escoga tipo de Gasolina Sin Plomo: ")
# Preguntem el tipus de gasolina SUPER, demanem els litres que voldrà i els multipliquem per el preu, ho mostrem per pantalla
    if (tipo_super==1) :
        print "Ha escogido Gasolina Sin Plomo Normal"
        litros=input("Introduzca los litros que desea comprar: ")
        if litros <=0 :
		    print "Ha introducido un numero erroneo."
        else :
            print "Ha introducido", litros , "l, el precio es de ", litros*1.6, "$"
    elif (tipo_super==2) :
        print "Ha escogido Gasolina Super Turbo"
        litros=input("Introduzca los litros que desea comprar: ")
        if litros <=0 :
		    print "Ha introducido un numero erroneo."
        else :
            print "Ha introducido", litros , "l, el precio es de ", litros*1.65, "$"
# Si escriu un numero erroni de gasolina, enviem missatge d'error    else :
    else :
        print "Ha introducido un numero erroneo."

# Si escull gasolina DIESEL (3) li preguntem quin tipus de DIESEL

elif (tipo_gasolina==3) :
    print "Ha elegido Gasolina Diesel"
    print """Que tipo de Gasolina Diesel quiere?
    Escriva 1 para Normal (1,70€/l)
    Escriva 2 para Fast&Fourius (1,75€/l)"""
    tipo_super=input("Escoga tipo de Gasolina Diesel: ")
# Preguntem el tipus de gasolina SUPER, demanem els litres que voldrà i els multipliquem per el preu, ho mostrem per pantalla
    if (tipo_super==1) :
        print "Ha escogido Gasolina Diesel Normal"
        litros=input("Introduzca los litros que desea comprar: ")
        if litros <=0 :
            print "Ha introducido un numero erroneo."
        else :
            print "Ha introducido", litros , "l, el precio es de ", litros*1.7, "$"
    elif (tipo_super==2) :
        print "Ha escogido Gasolina Diesel Fast"
        litros=input("Introduzca los litros que desea comprar: ")
        if litros <=0 :
		    print "Ha introducido un numero erroneo."
        else :
            print "Ha introducido", litros , "l, el precio es de ", litros*1.75, "$"
# Si escriu un numero erroni de gasolina, enviem missatge d'error
    else :
        print "Ha introducido un numero erroneo."

# Si escriu un numero erroni de gasolina, enviem missatge d'error

else:
    print "Ha introducido un numero erroneo."
