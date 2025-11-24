def utilidades():
    """Calcula porcentaje de utilidades según aportes"""
    print("\n=== EJERCICIO 23: Porcentaje de utilidades ===")

    capital_inicial = float(input("Capital inicial establecido: "))
    n = int(input("Número de socios: "))

    aportes = []
    suma_aportes = 0

    for i in range(n):
        nombre = input(f"Nombre del socio {i+1}: ")
        aporte = float(input(f"Aporte de {nombre}: "))
        aportes.append({"nombre": nombre, "aporte": aporte})
        suma_aportes += aporte

    if suma_aportes != capital_inicial:
        print(
            f"ERROR: La suma de aportes (${suma_aportes:.2f}) no coincide con el capital inicial (${capital_inicial:.2f})"
        )
        return

    print("\nPorcentaje de utilidades:")
    for socio in aportes:
        porcentaje = (socio["aporte"] / capital_inicial) * 100
        print(f"{socio['nombre']}: {porcentaje:.2f}%")


utilidades()
