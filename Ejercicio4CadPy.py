def quitarnumeros():
    telefono = input("Ingrese un número de teléfono con el formato Codpais-número-extensión: ")
    
    partes = telefono.split('-')
    
    numerosinpreniex = partes[1]
    

    print("El número sin prefijo ni extensión es:", numerosinpreniex)

quitarnumeros()
