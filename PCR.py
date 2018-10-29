
datos = open("WDBC.dat", "r")
or linea in datos:
    linea = linea.split(‘,’)
    print ‘Persona: ‘
    print ‘————‘
    print ‘Nombre: ‘ + linea[0] + ‘, Apellidos: ‘ + linea[1] + ‘, Edad: ‘ + linea[2]
    print ‘\n’

columna1 =datos[:,0]
columna2 =datos[:,1]
columna3 =datos[:,2]
columna4 =datos[:,3]

arreglo = np.ones((4,4))
resultado = 0
for i in range(4):
    for j in range(4):
        for k in range(len(datos[:,0])-1):
            resultado = ((datos[k,i] - media[i])*(datos[k,j]-media[j]))/tamano
            arreglo[i,j] = resultado
print (arreglo)
