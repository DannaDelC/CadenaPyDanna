def listadodeproductos():
    productos = input("Ingrese los productos de la cesta de la compra, separados por comas: ")

    listadeproductos = productos.split(',')
    
    print("\nProductos en la cesta:")
    for producto in listadeproductos:
        print(producto.strip()) 
listadodeproductos()
