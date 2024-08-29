def contletrasnombre():
    nombre = input("Ingrese su nombre: ")
    
    nommayusculas = nombre.upper()
    
    numletras = sum(1 for letra in nombre if letra.isalpha())
    
    mensaje = nommayusculas + " tiene " + str(numletras) + " letras."
    print(mensaje)

contletrasnombre()
