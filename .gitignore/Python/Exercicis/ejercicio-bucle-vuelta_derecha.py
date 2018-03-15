#coding: utf8
#Autor: Pol Balada
#15/3/18

#Fem que importi les comandes de LINUX i llençem la comanda clear perque el codi surti al inici del tot
import os
os.system("clear")


# Inicializaciones
salir = "N"
movimiento=1

while ( salir=="N" ):
    # Hago cosas
    if (movimiento>=1 and movimiento<=2) :
        print movimiento , "-> Arriba"
    elif (movimiento>=3 and movimiento<=4) :
        print movimiento , "-> Derecha"
    elif (movimiento>=5 and movimiento<=6) :
        print movimiento , "-> Abajo"
    elif (movimiento>=7 and movimiento<=8) :
        print movimiento , "-> Izquierda"
    # Incremento
    movimiento = movimiento + 1
    # Activo indicador de salida si toca
    if (movimiento>8 ): # Condición de salida
            salir = "S"
