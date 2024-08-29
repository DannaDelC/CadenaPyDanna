def resaltarvocal():
    frase = input("Ingrese una frase: ")
    vocal = input("Indique la vocal a resaltar: ")
    
    if vocal.lower() in 'aeiou' and len(vocal) == 1:
    
        frasesconv = frase.replace(vocal.lower(), vocal.upper())

        frasesconv = frasesconv.replace(vocal.upper(), vocal.upper())
    
        print("La frase modificada es:", frasesconv)
    else:
        print("Ingrese una única vocal (a, e, i, o, u).")

resaltarvocal()
