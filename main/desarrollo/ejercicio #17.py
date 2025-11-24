def estadistica():
    """Estadísticas de aprobación/reprobación por género"""
    print("\n=== EJERCICIO 17: Estadísticas de aprobación ===")

    hombres_aprobados = 0
    hombres_reprobados = 0
    mujeres_aprobadas = 0
    mujeres_reprobadas = 0

    while True:
        nombre = input("Nombre del estudiante (o 'fin' para terminar): ")
        if nombre.lower() == "fin":
            break

        genero = input("Género (H/M): ").upper()
        nota = float(input("Nota definitiva: "))

        if genero == "H":
            if nota >= 3.0:
                hombres_aprobados += 1
            else:
                hombres_reprobados += 1
        elif genero == "M":
            if nota >= 3.0:
                mujeres_aprobadas += 1
            else:
                mujeres_reprobadas += 1

    print(f"\nHombres aprobados: {hombres_aprobados}")
    print(f"Hombres reprobados: {hombres_reprobados}")
    print(f"Mujeres aprobadas: {mujeres_aprobadas}")
    print(f"Mujeres reprobadas: {mujeres_reprobadas}")


estadistica()
