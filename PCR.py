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

#Creo un arreglo de ceros con el tamaño de los datos
diferencias_medias = np.zeros(np.shape(datos))
#Creo un for que me recorra las variables y los datos para restarle a cada dato, su media correspondiente
for i in range( variables ):
    for j in range( ndatos ):
        diferencias_medias[i,j] = datos[i,j]-medias[i]

# En un arreglo de unos guardo la matriz de covarianza con tamaño 30x30 (variables a analizar)
arreglo = np.ones((variables,variables))
#Calculo la matriz de covarianza (np.sum((x-xMed)*(y-yMed))/n)
for i in range(variables):
    for j in range(variables):
        resultado = np.sum( diferencias_medias[i,:]*diferencias_medias[j,:] )/ndatos
        arreglo[i,j] = resultado

#Imprimo mi matriz de covarianza 30x30
print("Matriz de covarianza:")
for i in range(variables):
    print(arreglo[i,:])
#Del paquete de numpy uso linalg.eig para calcular mis autovalores y autovectores
autovalores, autovectores = np.linalg.eig(arreglo)
print("Autovectores y autovalores")
for i in range(variables):
    print("Autovalor", " ", i, " " ,autovalores[i])
    print("Autovector", "  ", i, autovectores[:,i])

print("Autovalores originales")
print(autovalores)

#Ordeno los autovectores de acuerdo a los autovalores
for i in range(variables):
    for j in range(i, variables):
        if autovalores[j] > autovalores[i]:
            a = autovalores[i].copy()
            autovalores[i] = autovalores[j]
            autovalores[j] = a
            
            v = autovectores[j].copy()
            autovectores[:,i] = autovectores[:,j]
            autovectores[:,j] = v

print("Autovalores ordenados")
print(autovalores)            

#Las variables mas importantes
cuantas_variables_mas_importantes = 3

for i in range(cuantas_variables_mas_importantes):
    mas_importante = 0
    for j in range(variables):
        if np.abs(autovectores[j,i]) > np.abs(autovectores[mas_importante,i]):
            mas_importante = j
    print(" Variable mas importante segun autovalor ", i, "es ", mas_importante)

#Proyecciones sobre ejes PC1 y PC2
#Extraigo los componentes principales
PC1 = autovectores[:,0]
PC2 = autovectores[:,1]

# Hacer producto punto de cada columna de datos con cada uno de los componentes principales que saqué anteriormente
datos_proyectados = np.ones((2,ndatos))*0
for k in range(ndatos):
    for i in range(variables):
        datos_proyectados[0,k] = datos_proyectados[0,k] + PC1[i]*datos[i,k]
        datos_proyectados[1,k] = datos_proyectados[1,k] + PC2[i]*datos[i,k]      
#print(np.shape(datos_proyectados))

