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

#Analisis de Fourier
#filtro pasa bajos con frecuencia de corte fc = 1000Hz
real, imaginario, frecuencias, filtrado1000 = analisis_fourier(signal[:,0], signal[:,1], fc=1000)
#500
real, imaginario, frecuencias, filtrado500 = analisis_fourier(signal[:,0], signal[:,1], fc=500)
#Interpolacion cuadrática para 500 y 1000
o2_real, o2_imaginario, o2_frecuencias, o2_filtrado1000 = analisis_fourier(xnuevo, interpolacion_o2, fc=1000)
o2_real, o2_imaginario, o2_frecuencias, o2_filtrado500 = analisis_fourier(xnuevo, interpolacion_o2, fc=500)
#Interpolacion cúbica para 500 y 1000
o3_real, o3_imaginario, o3_frecuencias, o3_filtrado1000 = analisis_fourier(xnuevo, interpolacion_o3, fc=1000)
o3_real, o3_imaginario, o3_frecuencias, o3_filtrado500 = analisis_fourier(xnuevo, interpolacion_o3, fc=500)

#Creo mi gŕafica con los datos de signal originales
plt.figure()
plt.plot(signal[:,:])
plt.title("Datos de signal")
plt.grid()
plt.savefig("CaceresNaranjoVanessa_signal.pdf")

#Hago el gráfico de mis frecuencias
plt.figure()
plt.plot(frecuencias, real**2+imaginario**2, c = "pink")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")
plt.grid()
plt.savefig("CaceresNaranjoVanessa_TF.pdf")
plt.xlim(-600,600)
print("bono","Frecuencias calculadas sin usar fftfreq")
print("En la grafica se ve que el armonico principal actua en una frecuencia alrededor de 160-180 Hz y otros dos armonicos ique se logran resaltar a una frecuencia de alrededor de 250 y  410 Hz")


# grafica de señal filtrada
plt.figure()
plt.plot(signal[:,0], filtrado1000, c = "r" )
plt.xlabel("Tiempo []")
plt.ylabel("Amplitud")
plt.grid()
plt.savefig("CaceresNaranjoVanessa_filtrado.pdf")
#Mensaje de que no se puede realizar la segunda transformada con incompletos
print("No se puede hacer la transformada de los datos incompletos.dat porque los datos de la variable del tiempo no estan bien espaciados")
#Graficar las frecuencias originales, con interpolacion cuadratica y con interpolacion cubica
plt.figure(figsize=(5,10))
plt.subplot(3,1,1)

plt.plot(frecuencias, real**2+imaginario**2, c = "purple")
plt.xlim(-1000,1000)
plt.title("original")
plt.ylabel("Amplitud")
plt.subplot(3,1,2)

plt.plot(o2_frecuencias, o2_real**2+o2_imaginario**2, c = "pink")
plt.xlim(-1000,1000)
plt.title("Interpolacion cuadrada")
plt.ylabel("Amplitud")
plt.subplot(3,1,3)
plt.plot(o3_frecuencias, o3_real**2+o3_imaginario**2, c = "green")
plt.xlim(-1000,1000)
plt.title("Interpolacion cubica")

plt.savefig("CaceresNaranjoVanessa_TF_interpola.pdf")

print("La interpolacion cuadrada agrega unas frecuencias de poca amplitud entre aproximadamente 500-1000 y disminuye el tercer pico desde 150000 hasta 80000 aproximadamente")
print("La interpolacion cubica disminuye la amplitud del tercer pico y agrega frecuencias de poca amplitud")

#Grafica de frecuencia de corte de 1000
plt.figure(figsize=(5,10))
plt.subplot(2,1,1)
plt.plot(signal[:,0], filtrado1000, label = "filtro orig", c = "r")
plt.plot(xnuevo, o2_filtrado1000, label = "cuadratica", c = "purple")
plt.plot(xnuevo, o3_filtrado1000, label ="cubica", c = "pink")
plt.legend()
plt.title("Grafica1")
plt.ylabel("Amplitud  despues de filtro a 1000")
#Grafica de frecuencia de corte de 500
plt.subplot(2,1,2)
plt.plot(signal[:,0], filtrado500, label = "filtro orig" , c = "green")
plt.plot(xnuevo, o2_filtrado500,label = "cuadratica", c = "red")
plt.plot(xnuevo, o3_filtrado500 , label ="cubica", c = "gold")
plt.title("Grafica2")
plt.legend()
plt.ylabel("Amplitud  despues de filtro a 500")
plt.savefig("CaceresNaranjoVanessa_2Filtros.pdf")
