def presupuesto():
    """Distribuye presupuesto estatal por rubros"""
    print("\n=== EJERCICIO 20: Presupuesto estatal ===")

    while True:
        año = input("Año (o 'fin' para terminar): ")
        if año.lower() == "fin":
            break

        presupuesto = float(input(f"Presupuesto para {año}: "))

        vivienda = presupuesto * 0.25
        educacion = presupuesto * 0.20
        armamento = presupuesto * 0.40
        salud = presupuesto * 0.15

        print(f"\nPresupuesto {año}:")
        print(f"  Vivienda (25%): ${vivienda:.2f}")
        print(f"  Educación (20%): ${educacion:.2f}")
        print(f"  Armamento (40%): ${armamento:.2f}")
        print(f"  Salud (15%): ${salud:.2f}")


presupuesto()
