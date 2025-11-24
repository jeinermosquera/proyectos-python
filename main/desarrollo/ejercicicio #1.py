# EJERCICIO 1: Aumento del 5% para trabajadores con sueldo < 500000
def aumento():
    """Liquida aumento del 5% para N trabajadores"""
    print("\n=== EJERCICIO 1: Aumento de sueldo ===")

    n = int(input("Número de trabajadores: "))

    for i in range(n):
        nombre = input(f"Nombre del trabajador {i+1}: ")
        sueldo = float(input(f"Sueldo actual de {nombre}: "))

        if sueldo < 500000:
            aumento = sueldo * 0.05
            nuevo_sueldo = sueldo + aumento
            print(
                f"{nombre}: Sueldo actual: ${sueldo:.2f} - Nuevo sueldo: ${nuevo_sueldo:.2f}"
            )
        else:
            print(
                f"{nombre}: Sueldo actual: ${sueldo:.2f} - No tiene derecho al aumento"
            )


aumento()
