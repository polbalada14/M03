# coding: utf8
# Autor: Pol Balada
# 16/3/18

#Fem que importi les comandes de LINUX i llençem la comanda clear perque el codi surti al inici del tot
import os
os.system("clear")


# Inicializaciones
salir = "N"
movimiento = 1
vueltas=input("Cuantas vueltas quieres dar? ")
giro = raw_input("Hacia que lado quieres girar? DERECHA(d)/IZQUIERDA(i) ")

while ( salir=="N" ):
    # Hago cosas
    if (movimiento%8==1 or movimiento%8==2) :
        print movimiento , "-> Arriba"
    elif (movimiento%8==3 or movimiento%8==4) :
        if( giro.lower() =="d" ) :
            print movimiento , "-> Derecha"
        else: #giro=="i"
            print movimiento, "-> Izquierda"
    elif (movimiento%8==5 or movimiento%8==6) :
        print movimiento , "-> Abajo"
    elif (movimiento%8==7 or movimiento%8==0) :
        if(giro.lower() =="d"):
            print movimiento , "-> Izquierda"
        else: #giro=="i"
            print movimiento, "-> Derecha"
    # Incremento
    movimiento = movimiento + 1
    # Activo indicador de salida si toca
    if (movimiento>vueltas*8): # Condición de salida
        salir = "S"
