# coding: utf8
# Autor: Pol Balada
# 11/3/18

#Fem que importi les comandes de LINUX i llençem la comanda clear perque el codi surti al inici del tot
import os
os.system("clear")

# Inicializaciones
salir = "N"
num = 1
suma = 0
print"""
BUCLE SUMAR
"""
while ( salir=="N" ):
    # Hago cosas
    print num,
    if (num<5): 
       print "+" , 
    # Incremento
    suma = suma + num
    num= num +1
    # Activo indicador de salida si toca
    if ( num>5 ): # Condición de salida
        salir = "S"
print "=" , suma
