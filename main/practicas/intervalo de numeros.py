print("\nPrograma que me permite mostrar el intervalo entre dos numeros:")
while True:  # validamos la entrada para qye el usuario solamente nos ingrese numeros.
    try:
        """
        utilizamos el try - except para capturar
        posibles errores del usuario.
        """
        numero1 = int(input("Ingrese el primer numero: "))
        break
    except ValueError:
        print("debes de ingresar numeros no letas ni simbolos, intentalo nuevamete.")


while True:  # validamos la entrada para qye el usuario solamente nos ingrese numeros.
    try:

        """
        utilizamos el try - except para capturar
        posibles errores del usuario.
        """
        numero2 = int(input("\nIngrese el segundo numero: "))
        break

    except ValueError:
        print("debes de ingresar numeros no letas ni simbolos, intentalo nuevamete.")


# Verificamos cual numero es mayor para que el bucle comienze del menor al mayor
if numero1 < numero2:
    for numero in range(numero1, numero2 + 1):
        print(numero)
elif numero1 > numero2:
    for numero in range(numero2, numero1 + 1):
        print(numero)
