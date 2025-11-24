def aumento():
    """Calcula aumento según tabla gubernamental"""
    print("\n=== EJERCICIO 6: Aumento según tabla ===")

    n = int(input("Número de trabajadores: "))

    for i in range(n):
        nombre = input(f"Nombre del trabajador {i+1}: ")
        sueldo = float(input(f"Sueldo de {nombre}: "))

        if sueldo < 265000:
            aumento = sueldo * 0.10
        elif sueldo < 450000:
            aumento = sueldo * 0.08
        else:
            aumento = sueldo * 0.05

        nuevo_sueldo = sueldo + aumento
        print(f"{nombre}: Nuevo sueldo: ${nuevo_sueldo:.2f}")


aumento()
