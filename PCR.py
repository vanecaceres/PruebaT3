import numpy as np
import csv
import matplotlib.pyplot as plt
from io import StringIO

datos = np.genfromtxt("WDBC.dat", delimiter = ",",unpack = True,  usecols = (0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31))
#print(datos)

columnas = []
for i in range(len(datos[:,0])):
    columnas.append(i)
    columnas[i] = datos[:,i]

medias = []
for i in range(len(datos[:,0])):
    medias.append(i)
    medias[i] = np.mean(columnas[i])

#print(len(datos[:,0]))

#tamano = len(datos[:,0])-1

arreglo = np.ones((31,31))
#print (arreglo)
resultado = 0

filas = len(datos[0,:])
columnas = len(datos[:,0])

for i in range(columnas-1):
    for j in range(filas):
        resultado = np.sum((datos[i,j]-medias[i])*(datos[i+1,j]-medias[i+1]))/tamano

print (resultado)

#Los parametros más importantes
print("Los parámetros más importantes")

  
