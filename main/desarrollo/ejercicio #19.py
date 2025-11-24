def pulsaciones():
    """Calcula pulsaciones por cada 10 segundos de ejercicio"""
    print("\n=== EJERCICIO 19: Pulsaciones por ejercicio ===")

    n = int(input("Número de personas: "))

    for i in range(n):
        nombre = input(f"Nombre de la persona {i+1}: ")
        edad = int(input(f"Edad de {nombre}: "))

        pulsaciones = (220 - edad) / 10

        print(f"{nombre} ({edad} años): {pulsaciones:.2f} pulsaciones por 10 segundos")


pulsaciones()
