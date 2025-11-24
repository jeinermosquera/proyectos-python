usuario = "jeiner mosquera"
contraseña = "Isaac2006"
while True:
    usuario_ingresado = str(input("\nIngrese su usuario:"))
    if usuario_ingresado == usuario:
        break
    else:
        print("Usuario incorrecto")
while True:
    contraseña_ingresada = str(input("Ingrese su contraseña: "))
    if len(contraseña_ingresada) == contraseña:
        if contraseña_ingresada == contraseña:
            print("Bienvenido al sistema")
            break
