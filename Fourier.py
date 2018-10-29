import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy.fftpack import ifft
from scipy.interpolate import interp1d
from io import StringIO

signal = np.genfromtxt("signal.dat",delimiter = ",", dtype=None, comments='#',unpack = True)

incompletos = np.genfromtxt("incompletos.dat",delimiter = ",",dtype=None, comments='#',unpack = True)

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
		imaginario[i]= variable[j]*np.sin(-2*np.pi*i*j/ndatos)
		
