while True:
    try:
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        if numero1 < 0 or numero2 < 0:
            print(" debes de ingresar un numero positivio, intetalo nuevamente.")
        else:
            break
    except ValueError:
        print(
            "debes de ingresar un numero no letras ni simbolos, intentalo nuevamente."
        )
