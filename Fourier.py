import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy.fftpack import ifft
from scipy.interpolate import interp1d
from io import StringIO



signal = np.genfromtxt('signal.dat', dtype=None, comments='#', delimiter=',',unpack = False)
incompletos = np.genfromtxt('incompletos.dat', dtype=None, comments='#', delimiter=',', unpack = False)

filasIncompletos = []
columnasIncompletos = []

#print(len(incompletos[1,:]),len(incompletos[:,1]))
columna1I = (incompletos[0,:])
columna2I = (incompletos[1,:])

#Funcion que devuelve la transformada de fourier y el espectro de frecuencias
def analisis_fourier(tiempo, variable, fc):
#Numero de datos 
    ndatos = len(variable) 
#Creo un arreglo de ceros del tamaño que me entre para los numeros reales e imaginarios
    real = np.zeros(np.shape(variable))
    imaginario = np.zeros(np.shape(variable))

    for i in range(len(variable)):
        imaginario[i]=0
        real[i] =0
        for j in range(len(variable)):
            #Me va a ir sumando los valores
            imaginario[i]= imaginario[i] + variable[j]*np.sin(-2*np.pi*i*j/ndatos)
            real[i] = real[i] + variable[j]*np.cos(-2*np.pi*i*j/ndatos)

    #Calculo las frecuencias
    frecuencias = np.zeros(np.shape(variable))
    #Calculo mi periodo
    periodo_muestreo = tiempo[1]-tiempo[0] 

    #Creo una variable que me guarde la mitad del tamañod de los datos
    n2 = int(ndatos/2)
    #Calculo la maxima frecuencia
    fmaxima = (1.0/2.0)*1.0/periodo_muestreo
    delta_frecuencia = fmaxima/n2

    #Lleno mi vector de frecuencias con los valores
    frecuencias[0:n2] = np.arange(delta_frecuencia, fmaxima+delta_frecuencia, delta_frecuencia)
    frecuencias[n2:] = np.arange(-fmaxima, -delta_frecuencia+delta_frecuencia, delta_frecuencia)

    realfiltrado = np.zeros(np.shape(variable))
    imaginariofiltrado = np.zeros(np.shape(variable))
    
    # Filtrar la senal
    for i in range(ndatos):
        if -fc < frecuencias[i] and frecuencias[i] < fc:
            # Valores para conservar porque estan en la banda
            realfiltrado[i] = real[i]
            imaginariofiltrado[i] = imaginario[i]
        elif frecuencias[i] < -fc or fc < frecuencias[i]:
            # Valores para eliminar porque estan fuera de la banda de frecuencias
            realfiltrado[i] = real[i]*1e-3
            imaginariofiltrado[i] = imaginario[i]*1e-3

    
    filtrado = ifft(realfiltrado + 1j*imaginariofiltrado)
    # retornar las varialbes de interes
    return real, imaginario, frecuencias, filtrado.real

real, imaginario, frecuencias, filtrado = analisis_fourier(signal[:,0], signal[:,1], fc=1000)


#Hago el gráfico de mis frecuencias
plt.figure()
plt.plot(frecuencias, real**2+imaginario**2)



