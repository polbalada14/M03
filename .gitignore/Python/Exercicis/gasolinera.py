# coding: utf8
# Autor: Pol Balada
# 21/2/18

print """Bienvenido a la gasolinera,
¿que tipo de gasolina quiere?

 -Escriva 1 para Super: Normal (1,50€), Turbo (1,55€)
 -Escriva 2 para Sin plomo: Normal (1,60€), Con aditivo de sabor naranja (1,65€)
 -Escriva 3 para Diesel: Normal (1,70€), Fast&Fourious (1,75€)"""

tipo_gasolina=input("Introduzca tipo de gasolina: ")

if (tipo_gasolina==1) :
    print "Ha elegido Gasolina Super"
    print """Que tipo de Gasolina super quiere?
    Escriva 1 para Normal (1,50€/l)
    Escriva 2 para Turbo (1,55€/l)"""
    tipo_super=input("Escoga tipo de Gasolina super: ")
    if (tipo_super==1) :
        print "Ha escogido Gasolina Super Normal"
        litros_super_normal=input("Introduzca los litros que desea comprar: ")
        print "Ha introducido", litros_super_normal , "l, el precio es de ", litros_super_normal*1.5, "$"
    elif (tipo_super==2) :
        print "Ha escogido Gasolina Super Turbo"
        litros_super_turbo=input("Introduzca los litros que desea comprar: ")
        print "Ha introducido", litros_super_turbo , "l, el precio es de ", litros_super_turbo*1.55, "$"
    else :
        print "Ha introducido un numero erroneo."
elif (tipo_gasolina==2) :
    print "Ha elegido Gasolina Sin Plomo"
    print """Que tipo de Gasolina Sin Plomo quiere?
    Escriva 1 para Normal (1,60€/l)
    Escriva 2 para Con aditivo de sabor naranja (1,65€/l)"""
    tipo_super=input("Escoga tipo de Gasolina Sin Plomo: ")
    if (tipo_super==1) :
        print "Ha escogido Gasolina Sin Plomo Normal"
        litros_sinplomo_normal=input("Introduzca los litros que desea comprar: ")
        print "Ha introducido", litros_sinplomo_normal , "l, el precio es de ", litros_sinplomo_normal*1.6, "$"
    elif (tipo_super==2) :
        print "Ha escogido Gasolina Super Turbo"
        litros_sinplomo_add=input("Introduzca los litros que desea comprar: ")
        print "Ha introducido", litros_sinplomo_add , "l, el precio es de ", litros_sinplomo_add*1.65, "$"
    else :
        print "Ha introducido un numero erroneo."
elif (tipo_gasolina==3) :
    print "Ha elegido Gasolina Diesel"
    print """Que tipo de Gasolina Diesel quiere?
    Escriva 1 para Normal (1,70€/l)
    Escriva 2 para Fast&Fourius (1,75€/l)"""
    tipo_super=input("Escoga tipo de Gasolina Diesel: ")
    if (tipo_super==1) :
        print "Ha escogido Gasolina Diesel Normal"
        litros_diesel_normal=input("Introduzca los litros que desea comprar: ")
        print "Ha introducido", litros_diesel_normal , "l, el precio es de ", litros_diesel_normal*1.7, "$"
    elif (tipo_super==2) :
        print "Ha escogido Gasolina Diesel Fast"
        litros_diesel_fast=input("Introduzca los litros que desea comprar: ")
        print "Ha introducido", litros_diesel_fast , "l, el precio es de ", litros_diesel_fast*1.75, "$"
    else :
        print "Ha introducido un numero erroneo."
else:
    print "Ha introducido un numero erroneo."
