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

# quito el primer dato porque no es una medicion ya que es un valor demasiado grande y me daña mis calculos
datos = datos[1:,:] 
#print(np.shape(datos))
#Asigno variables y numero de datos 30,569
variables, ndatos = np.shape(datos)
#Caculo las medias de cada variable con un for que me las recorra todas
medias = []
for i in range(variables): 
    #Calcula la media como la suma de datos/numero de datos
    medias.append( np.sum(datos[i,:])/ndatos ) 


