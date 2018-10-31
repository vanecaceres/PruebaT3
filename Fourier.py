import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy.fftpack import ifft
from scipy.interpolate import interp1d
from io import StringIO

#Importo los datos de signal.dat
signal = np.genfromtxt("signal.dat", dtype=None, comments="#", delimiter=",",unpack = False)
#Importo los datos desde incompletos.dat
incompletos = np.genfromtxt("incompletos.dat", dtype=None, comments="#", delimiter=",", unpack = False)

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
#Arreglo de ceros imaginarios
    imaginario = np.zeros(np.shape(variable))
#Hago dos for que me recorran el tamaño que me entra por parametro
    for i in range(len(variable)):
        imaginario[i]=0
        real[i] =0
        for j in range(len(variable)):
            #Me va a ir sumando los valores bk
            imaginario[i]= imaginario[i] + variable[j]*np.sin(-2*np.pi*i*j/ndatos)
		#Me conformal la funcion de ak
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
    #Hago dos arreglos de ceros de nuevo con el tamño de la variable que me entra por parametro para mis reales e imaginarios pero ahora infiltrados
    realfiltrado = np.zeros(np.shape(variable))
    imaginariofiltrado = np.zeros(np.shape(variable))
    
    #Voy a comenzar a filtrar la señal que se encuentre entre +,- la frecuencia que me entra por restriccion
    for i in range(ndatos):
        if -fc < frecuencias[i] and frecuencias[i] < fc:
            # Valores para conservar porque estan en dentro de las condiciones
            realfiltrado[i] = real[i]
            imaginariofiltrado[i] = imaginario[i]
        elif frecuencias[i] < -fc or fc < frecuencias[i]:
            # Valores para eliminar porque estan fuera de la banda de frecuencias
            realfiltrado[i] = real[i]*1e-3
            imaginariofiltrado[i] = imaginario[i]*1e-3

    
    filtrado = ifft(realfiltrado + 1j*imaginariofiltrado)
    #Devuelvo los valores que necesito
    return real, imaginario, frecuencias, filtrado.real


def interpolaciones(x, y, n_nuevo_datos):
    #Creo la interpolación
    #Cuadrática
    interpolacion_o2 = interp1d(x, y, kind='quadratic')
    #cúbica
    interpolacion_o3 = interp1d(x, y, kind='cubic')
    
    #Mi linspace con los x que voy a interpolar
    xnuevo = np.linspace(x[0], x[-1], n_nuevo_datos)
    
    return xnuevo, interpolacion_o2(xnuevo), interpolacion_o3(xnuevo)
    

# Crear datos interpolados para mis datos incompletos
xnuevo, interpolacion_o2, interpolacion_o3 = interpolaciones(incompletos[:,0], incompletos[:,1], 512)


