def neumatico():
    """Calcula masa de aire en N neumáticos"""
    print("\n=== EJERCICIO 18: Masa de aire ===")

    n = int(input("Número de neumáticos: "))

    for i in range(n):
        print(f"\nNeumático {i+1}:")
        volumen = float(input("Volumen (pies cúbicos): "))
        presion = float(input("Presión: "))
        temperatura = float(input("Temperatura: "))

        masa = (presion * volumen) / (0.37 * temperatura + 460)

        print(f"Masa de aire: {masa:.4f}")


neumatico()
