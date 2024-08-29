def imprimnomveces():
    nombre = input("Ingrese su nombre: ")
    numero = int(input("Ingrese un número entero: "))
    
    for _ in range(numero):
        print(nombre)

imprimnomveces()
