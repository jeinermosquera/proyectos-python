def calculo():
    """Calcula incremento del 6% y bonificación del 10% según condiciones"""
    print("\n=== EJERCICIO 3: Incremento y bonificación ===")

    n = int(input("Número de trabajadores: "))

    for i in range(n):
        nombre = input(f"Nombre del trabajador {i+1}: ")
        sueldo = float(input(f"Sueldo de {nombre}: "))

        # Incremento del 6%
        incremento = sueldo * 0.06
        nuevo_sueldo = sueldo + incremento

        # Bonificación si el nuevo sueldo < 380000
        bonificacion = 0
        if nuevo_sueldo < 380000:
            bonificacion = nuevo_sueldo * 0.10
            sueldo_final = nuevo_sueldo + bonificacion
        else:
            sueldo_final = nuevo_sueldo

        print(f"{nombre}:")
        print(f"  Sueldo original: ${sueldo:.2f}")
        print(f"  Incremento (6%): ${incremento:.2f}")
        print(f"  Nuevo sueldo: ${nuevo_sueldo:.2f}")
        if bonificacion > 0:
            print(f"  Bonificación (10%): ${bonificacion:.2f}")
        print(f"  Sueldo final: ${sueldo_final:.2f}")


calculo()
