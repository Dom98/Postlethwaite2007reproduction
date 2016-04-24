# -*- coding: utf-8 -*-

#script which is finding the real conductance of AMPA channel
import csv
import matplotlib.pyplot as plt

name1 = "AMPAR_O1.World.dat"
name2 = "AMPAR_O2.World.dat"
name3 = "AMPAR_O3.World.dat"
name4 = "AMPAR_O4.World.dat"
name =  "AMPA_001_001.dat"

gmax4 = 34*10e-12 # pS
gmax3 = 0.7 * gmax4
gmax2 = 0.4 * gmax4
gmax1 = 0.1 * gmax4

lista = []
listaO= []

csv_reader = csv.reader(open(name4), delimiter=" ")
for row in csv_reader:
    row = float(row[0]), float(row[1])
    lista.append(gmax4*row[1])
    listaO.append(row[1])

counter=0    
csv_reader = csv.reader(open(name3), delimiter=" ")
for row in csv_reader:
    row = float(row[0]), float(row[1])
    lista[counter]=lista[counter]+gmax3*row[1]
    listaO[counter]=listaO[counter]+row[1]
    counter+=1

counter=0
csv_reader = csv.reader(open(name2), delimiter=" ")
for row in csv_reader:
    row = float(row[0]), float(row[1])
    lista[counter]=lista[counter]+gmax2*row[1]
    listaO[counter]=listaO[counter]+row[1]
    counter+=1    
    
counter=0
csv_reader = csv.reader(open(name1), delimiter=" ")
for row in csv_reader:
    row = float(row[0]), float(row[1])
    lista[counter]=lista[counter]+gmax1*row[1]
    listaO[counter]=listaO[counter]+row[1]
    counter+=1 

# writing data to file

file0 = open(str(name), 'w')
counter=0
listat=[]
for i in lista:
    file0.write(str(counter*1e-06))
    file0.write(" ")
    file0.write(str(i))
    file0.write("\n")
    listat.append(counter)
    counter+=1
file0.close()

