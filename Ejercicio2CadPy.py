def mostnomformatos():
    nomcompleto = input("Ingrese su nombre completo: ")
    
    nomminusculas = nomcompleto.lower()
    
    nommayusculas = nomcompleto.upper()
    
    nomcombinado = nomcompleto.title()
    
    print("\nNombre en minúsculas: ", nomminusculas)
    print("Nombre en mayúsculas: ", nommayusculas)
    print("Nombre con mayúsculas en las iniciales: ", nomcombinado)

mostnomformatos()
