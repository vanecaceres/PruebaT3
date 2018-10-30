import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from scipy import fftpack
from scipy.interpolate import interp1d

#Cargo la imagen del arbol
arbol_numpy = img.imread("arbol(1).png")
#Transformada de fourier en 2D
arbol_fourier = fftpack.fft2(arbol_numpy)
#Creo una imagen y la guardo
plt.figure()
plt.imshow(np.log(np.abs(arbol_fourier)))
#Guardo la imagen
plt.savefig("CaceresNaranjoVanessa_FT2D.pdf")

# Angulo de las elipses que conforman el filtro de la imagen en las dos esquinas
alpha = -np.pi/10

# Genero mi X y Y con las posiciones de cada punto en la imagen
X,Y = np.meshgrid(range(len(arbol_fourier)), range(len(arbol_fou0rier)))
#Primera elipse
# Desplazar mi X y Y para ubicar cada elipse con un numero aproximado a la ubicacion
#Costado superior izquierdo porque mi 0 esta en la esquina superior izquierda
Xdesplazado = X - 45
Ydesplazado = Y - 45

#Igualo a cero los armonicos dentro de cada elipse
arbol_fourier[ (Xdesplazado*np.cos(alpha) + Ydesplazado*np.sin(alpha))**2/1 + (Xdesplazado*np.sin(alpha) - Ydesplazado*np.cos(alpha))**2/5 < 250] = 0
#Menor a 250 porque es el tamaño total de la imagen

#Segunda elipse
#Desplazar de nuevo para ubicar la elipse, en este caso en el costado inferior derecho
#Mi 250 que es el valor total está en la esquina derecha inferior
Xdesplazado = X - 180
Ydesplazado = Y - 220
arbol_fourier[ (Xdesplazado*np.cos(alpha) + Ydesplazado*np.sin(alpha))**2/1 + (Xdesplazado*np.sin(alpha) - Ydesplazado*np.cos(alpha))**2/5 < 250] = 0
