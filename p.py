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

import urllib.request
 
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
 
req = urllib.request.Request('https://arstechnica.com', headers = headers)
html = urllib.request.urlopen(req).read()
print(html)

