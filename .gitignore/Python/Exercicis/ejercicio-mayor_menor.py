# coding: utf8
# Autor: Pol Balada
# 9/2/18

A=input ("Introdueix un numero (no repetir)")
B=input ("Introdueix un numero (no repetir)")
C=input ("Introdueix un numero (no repetir)")

if (A==B)or(A==C)or(B==C) :
    print "Hi ha valors repetits"
else :
    if (A>B)and(A>C) :
        if B>C :
            print "A es el mes gran i C es el mes petit"
	    else :
            print "A es el mes gran i B es el mes petit"
    else :
        if (B>A) and (B>C) :
            if A>C :
                print "B es el mes gran i C es el mes petit"
            else :
                print "B es el mes gran i A es el mes petit"
        else
            if B>A :
                print "C es el mes gran i A es el mes petit"
            else :
                print "C es el mes gran i B es el mes petit"
