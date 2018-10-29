#Fourier
import numpy as np
import csv
import matplotlib.pyplot as plt
from io import StringIO

signal = np.genfromtxt("signal.dat","r")

incompletos = np.genfromtxt("incompletos.dat","r")

filasIncompletos = []
columnasIncompletos = []
for i in range(len(incompletos[:,1]):
	for j in range(len(incompletos[:,1]):
		filasIncompletos[i] = incompletos[i,:]
		columnasIncompletos[j] = incompletos[:,j]
		
		filasSignal[i] = signal[i,:]
		columnasSignal[j] = signal[:,j]
