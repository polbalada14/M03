# coding: utf8
# Autor: Pol Balada
# 9/2/18

dividendo=input("Escriba el dividendo: ")
divisor=input("Escriba el divisor: ")

#Escrivim menor o igual a zero perque no es pot dividir entre 0 o un numero negatiu, i enviem missatge d'error.
if divisor<=0 :
    print "No es pot dividir entre 0 o un numero menor de zero."
else :
    if dividendo%divisor==0 :
        print "La division es exacta. Cociente: ", dividendo//divisor
    else :
        print "La division no es exacta. Cociente: ", dividendo//divisor , "Resto: " , dividendo%divisor
