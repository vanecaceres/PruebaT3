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
