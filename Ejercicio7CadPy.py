def cambiarfinal():
    correo = input("Ingrese su correo electrónico: ")
    
    nombreusuario = correo.split('@')[0]
    
    nuevocorreo = nombreusuario + '@ceu.es'
    
    print("Tu nuevo correo es:", nuevocorreo)

cambiarfinal()
