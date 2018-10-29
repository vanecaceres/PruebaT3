import numpy as np
import csv
import matplotlib.pyplot as plt
from io import StringIO

signal = np.genfromtxt("signal.dat",delimiter = ",",unpack = True)

incompletos = np.genfromtxt("incompletos.dat",delimiter = ",",unpack = True)

filasIncompletos = []
columnasIncompletos = []

print(len(incompletos[1,:]),len(incompletos[:,1]))
columna1I = (incompletos[0,:])
columna2I = (incompletos[1,:])

x = np.linspace(-4,-4,100)
#plt.plot(incompletos,signal)


for i in range(len(incompletos[:,1])):
    for j in range(len(incompletos[1,:])):
                   
        filasIncompletos[i] = incompletos[i,:]
        columnasIncompletos[j] = incompletos[:,j]
        
        filasSignal[i] = signal[i,:]
        columnasSignal[j] = signal[:,j]
