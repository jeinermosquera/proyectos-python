def comparacion():
    """Compara dos números repetidamente hasta que el usuario desee salir"""
    print("\n=== EJERCICIO 5: Comparar números ===")

    while True:
        num1 = float(input("Primer número: "))
        num2 = float(input("Segundo número: "))

        if num1 > num2:
            print(f"El mayor es: {num1}, el menor es: {num2}")
        elif num2 > num1:
            print(f"El mayor es: {num2}, el menor es: {num1}")
        else:
            print("Los números son iguales")

        continuar = input("¿Desea continuar? (s/n): ").lower()
        if continuar != "s":
            break


comparacion()
