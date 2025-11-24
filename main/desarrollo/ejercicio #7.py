def can_nmeros():
    """Clasifica N números enteros"""
    print("\n=== EJERCICIO 7: Clasificar números ===")

    n = int(input("Cantidad de números a evaluar: "))

    for i in range(n):
        numero = int(input(f"Número {i+1}: "))

        if numero > 0:
            print(f"{numero} es positivo")
        elif numero < 0:
            print(f"{numero} es negativo")
        else:
            print(f"{numero} es nulo")


can_nmeros()
