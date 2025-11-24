def intereses():
    """Calcula intereses bancarios al 18% anual"""
    print("\n=== EJERCICIO 13: Intereses bancarios ===")

    while True:
        nombre = input("Nombre del ciudadano (o 'fin' para terminar): ")
        if nombre.lower() == "fin":
            break

        ahorro = float(input("Cantidad de ahorro: "))
        meses = int(input("Número de meses: "))

        interes_anual = 0.18
        interes_mensual = interes_anual / 12
        interes_total = ahorro * interes_mensual * meses

        print(f"{nombre}: Interés ganado en {meses} meses: ${interes_total:.2f}")


intereses()
