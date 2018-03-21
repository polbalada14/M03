#coding: utf8
#Autor: Pol Balada
#15/3/18

#Fem que importi les comandes de LINUX i llençem la comanda clear perque el codi surti al inici del tot
import os
os.system("clear")
#Fem que importi time per usar el modul de temps
import time

# Inicializaciones
salir = "N"
movimiento=1
voltes=input("Quantes voltes vols donar? ")
sentit_volta=input("Cap a quin sentit vols que es fagi la volta? 1-Sentit de les agulles del rellotge, 2-Contrari a les agulles del rellotge")
os.system("clear")

while ( salir=="N" ):
    # Hago cosas
    if (sentit_volta==1):
        if (movimiento%8==1) :
            print """
            O O O
            X   O
            O O O
            """
            time.sleep (0.3)
            os.system("clear")
        elif (movimiento%8==2):
            print """
            X O O
            O   O
            O O O
            """
            time.sleep (0.3)
            os.system("clear")
        elif (movimiento%8==3):
            print """
            O X O
            O   O
            O O O
            """
            time.sleep (0.3)
            os.system("clear")
        elif (movimiento%8==4):
            print """
            O O X
            O   O
            O O O
            """
            time.sleep (0.3)
            os.system("clear")
        elif (movimiento%8==5):
            print """
            O O O
            O   X
            O O O
            """
            time.sleep (0.3)
            os.system("clear")
        elif (movimiento%8==6):
            print """
            O O O
            O   O
            O O X
            """
            time.sleep (0.3)
            os.system("clear")
        elif (movimiento%8==7):
            print """
            O O O
            O   O
            O X O
            """
            time.sleep (0.3)
            os.system("clear")
        elif (movimiento%8==0):
            print """
            O O O
            O   O
            X O O
            """
            time.sleep (0.3)
            os.system("clear")
    if (sentit_volta==2):
        if (movimiento%8==1) :
            print """
            O O O
            X   O
            O O O
            """
            time.sleep (0.3)
            os.system("clear")
        elif (movimiento%8==2):
            print """
            O O O
            O   O
            X O O
            """
            time.sleep (0.3)
            os.system("clear")
        elif (movimiento%8==3):
            print """
            O O O
            O   O
            O X O
            """
            time.sleep (0.3)
            os.system("clear")
        elif (movimiento%8==4):
            print """
            O O O
            O   O
            O O X
            """
            time.sleep (0.3)
            os.system("clear")
        elif (movimiento%8==5):
            print """
            O O O
            O   X
            O O O
            """
            time.sleep (0.3)
            os.system("clear")
        elif (movimiento%8==6):
            print """
            O O X
            O   O
            O O O
            """
            time.sleep (0.3)
            os.system("clear")
        elif (movimiento%8==7):
            print """
            O X O
            O   O
            O O O
            """
            time.sleep (0.3)
            os.system("clear")
        elif (movimiento%8==0):
            print """
            X O O
            O   O
            O O O
            """
            time.sleep (0.3)
            os.system("clear")
    # Incremento
    movimiento = movimiento + 1
    # Activo indicador de salida si toca
    if (movimiento>voltes*8 ): # Condición de salida
         salir = "S"
