# coding: utf8
# Autor: Pol Balada
# 2/3/18

#Fem que importi les comandes de LINUX i llençem la comanda clear perque el codi surti al inici del tot
import os
os.system("clear")

print"""
BUCLE CONTAR
"""
# Inicializaciones
salir = "N"
num=input("A partir de quant vols contar? ")
limit=input("Fins a quant vols contar? ")

while ( salir=="N" ):
    # Hago cosas
    print num

    # Incremento
    num = num + 1
    # Activo indicador de salida si toca
    if ( num>limit ): # Condición de salida
            salir = "S"
