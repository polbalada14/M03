# coding: utf8
# Autor: Pol Balada
# 20/2/18

cajon1="movil"
cajon2="bocadillo"
cajon3="boli"
cajon4="bebida"

cajontmp=cajon1
cajon1=cajon3
cajon3=cajontmp
cajontmp=cajon4
cajon4=cajon2
cajon2=cajontmp

print "Cajon 1 ", cajon1
print "Cajon 2 ", cajon2
print "Cajon 3 ", cajon3
print "Cajon 4 ", cajon4
