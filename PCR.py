
file = open("WDBC.dat", "r")
or linea in file:
    linea = linea.split(‘,’)
    print ‘Persona: ‘
    print ‘————‘
    print ‘Nombre: ‘ + linea[0] + ‘, Apellidos: ‘ + linea[1] + ‘, Edad: ‘ + linea[2]
    print ‘\n’


arreglo = np.ones((4,4))
resultado = 0
for i in range(4):
    for j in range(4):
        for k in range(len(datos[:,0])-1):
            resultado = ((datos[k,i] - media[i])*(datos[k,j]-media[j]))/tamano
            arreglo[i,j] = resultado
print (arreglo)
