
file = open("WDBC.dat", "r")
or linea in file:
    linea = linea.split(‘,’)
    print ‘Persona: ‘
    print ‘————‘
    print ‘Nombre: ‘ + linea[0] + ‘, Apellidos: ‘ + linea[1] + ‘, Edad: ‘ + linea[2]
    print ‘\n’
