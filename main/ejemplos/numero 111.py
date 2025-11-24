while True:
    try:
        """
        utilizamos el try - except para capturar
        posibles errores del usuario.
        """
        numero = int(input("Ingrese el numero 111: "))
        if numero != 111:
            print("Debes ingresar el numero indicado para salir, intentalo nuevamente.")
        else:
            print("Saliendo del progama.")
            break
    except ValueError:
        print(
            "El debes de ingresar el numero indicado no letras o signos, intetalo de nuevo. "
        )
