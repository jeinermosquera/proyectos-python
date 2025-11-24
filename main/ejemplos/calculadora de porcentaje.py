# Programa que nos permite calcular el porcentaje a un numero.

while True:  # validamos la entrada para qye el usuario solamente nos ingrese numeros.
    try:
        """
        utilizamos el try - except para capturar
        posibles errores del usuario.

        """
        numero = float(
            input("\nIngrese el numero que desea calcularle el porcentaje: ")
        )
        if numero == 0:
            print("Ingresa un numero distito a cero, intentalo de nuevo.")
        else:
            break
    except:
        print("Debes de ingresar numeros no letras ni simbolos, intentalo nuevamente.")


while True:  # validamos la entrada para qye el usuario solamente nos ingrese numeros.
    try:
        """
        utilizamos el try - except para capturar
        posibles errores del usuario.

        """
        porcentaje = float(input("Ingrese el porcentaje que desea sacarle a numero: "))
        if porcentaje == 0:
            print("Debes de ingresar un numero disttinto a cero, intentalo nuevamente.")
        else:
            break
    except:
        print("debes de ingresar numeros no letas ni simbolos, intentalo nuevamete.")

# Realizamos los cálculos
resultado = numero * porcentaje / 100
print(
    f"El {porcentaje}% de {numero} es: {resultado}"
)  # Mostramos ell resultado en pantalla
