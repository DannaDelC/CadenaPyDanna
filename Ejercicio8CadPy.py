def separarprecio():
    precio = input("Ingrese el precio del producto en euros: ")
    
    euros, centimos = precio.split('.')
    

    print(f"El precio tiene {euros} euros y {centimos} céntimos.")

separarprecio()
