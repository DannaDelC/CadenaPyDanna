def separarfecha():
    fecha = input("Ingrese su fecha de nacimiento primero, dia, luego mes y por último año: ")
    
    if len(fecha) == 10 and fecha[2] == '/' and fecha[5] == '/':
        

        dia, mes, ano = fecha.split('/')
        
    
        print(f"Día: {dia.zfill(2)}")
        print(f"Mes: {mes.zfill(2)}")
        print(f"Año: {ano}")
    else:
        print("El formato de la fecha es incorrecto. Debe ser dia/mes/año.")

separarfecha()
