Hola esta es la prueba del repositorio.

Covarianza

for i in range(datos):
	columna[i] =datos[:,i]


arreglo = np.ones((4,4))
resultado = 0
for i in range(4):
    for j in range(4):
        for k in range(len(datos[:,0])-1):
            resultado = ((datos[k,i] - media[i])*(datos[k,j]-media[j]))/tamano
            arreglo[i,j] = resultado
print (arreglo)

