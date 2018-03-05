#coding: utf8
#Autor: Pol Balada
#22/2/18

#Fem que importi les comandes de LINUX i llençem la comanda clear perque el codi surti al inici del tot
import os
os.system("clear")

#Introduim un titol XULO
titulo="""
 BIENVENIDO A LA CALCULADORA IP 
"""
print titulo.center(100, "=")

netmask=input("Introdueix la netmask: ")

if (netmask<=0) :
    print "ERROR"
elif (netmask==1) :
    print "La mascara es: 128.0.0.0"
elif (netmask==2) :
    print "La mascara es: 192.0.0.0"
elif (netmask==3) :
    print "La mascara es: 224.0.0.0"
elif (netmask==4) :
    print "La mascara es: 240.0.0.0"
elif (netmask==5) :
    print "La mascara es: 248.0.0.0"
elif (netmask==6) :
    print "La mascara es: 252.0.0.0"
elif (netmask==7) :
    print "La mascara es: 254.0.0.0"
elif (netmask==8) :
    print "La mascara es: 255.0.0.0"
elif (netmask==9) :
    print "La mascara es: 255.128.0.0"
elif (netmask==10) :
    print "La mascara es: 255.192.0.0"
elif (netmask==11) :
    print "La mascara es: 255.224.0.0"
elif (netmask==12) :
    print "La mascara es: 255.240.0.0"
elif (netmask==13) :
    print "La mascara es: 255.248.0.0"
elif (netmask==14) :
    print "La mascara es: 255.252.0.0"
elif (netmask==15) :
    print "La mascara es: 255.254.0.0"
elif (netmask==16) :
    print "La mascara es: 255.255.0.0"
elif (netmask==17) :
    print "La mascara es: 255.255.128.0"
elif (netmask==18) :
    print "La mascara es: 255.255.192.0"
elif (netmask==19) :
    print "La mascara es: 255.255.224.0"
elif (netmask==20) :
    print "La mascara es: 255.255.240.0"
elif (netmask==21) :
    print "La mascara es: 255.255.248.0"
elif (netmask==22) :
    print "La mascara es: 255.255.252.0"
elif (netmask==23) :
    print "La mascara es: 255.255.254.0"
elif (netmask==24) :
    print "La mascara es: 255.255.255.0"
elif (netmask==25) :
    print "La mascara es: 255.255.255.128"
elif (netmask==26) :
    print "La mascara es: 255.255.255.192"
elif (netmask==27) :
    print "La mascara es: 255.255.255.224"
elif (netmask==28) :
    print "La mascara es: 255.255.255.240"
elif (netmask==29) :
    print "La mascara es: 255.255.255.248"
elif (netmask==30) :
    print "La mascara es: 255.255.255.252"
elif (netmask==31) :
    print "La mascara es: 255.255.255.254"
elif (netmask==32) :
    print "La mascara es: 255.255.255.255, aquesta mascara no pot navegar per internet"
else :
 print "Netmask erronea"
