def encuesta():
    """Captura datos de personas y calcula estadísticas por género"""
    print("\n=== EJERCICIO 2: Estadísticas por género ===")

    hombres = []
    mujeres = []

    while True:
        genero = input("Género (H/M) o 'fin' para terminar: ").upper()
        if genero == "FIN":
            break

        if genero in ["H", "M"]:
            edad = int(input("Edad: "))
            peso = float(input("Peso (kg): "))
            estatura = float(input("Estatura (m): "))

            datos = {"edad": edad, "peso": peso, "estatura": estatura}

            if genero == "H":
                hombres.append(datos)
            else:
                mujeres.append(datos)

    # Estadísticas
    print(f"\nNúmero de hombres: {len(hombres)}")
    print(f"Número de mujeres: {len(mujeres)}")

    if hombres:
        print(
            f"Edad promedio hombres: {sum(h['edad'] for h in hombres) / len(hombres):.2f}"
        )
        print(
            f"Peso promedio hombres: {sum(h['peso'] for h in hombres) / len(hombres):.2f}"
        )
        print(
            f"Estatura promedio hombres: {sum(h['estatura'] for h in hombres) / len(hombres):.2f}"
        )

    if mujeres:
        print(
            f"Edad promedio mujeres: {sum(m['edad'] for m in mujeres) / len(mujeres):.2f}"
        )
        print(
            f"Peso promedio mujeres: {sum(m['peso'] for m in mujeres) / len(mujeres):.2f}"
        )
        print(
            f"Estatura promedio mujeres: {sum(m['estatura'] for m in mujeres) / len(mujeres):.2f}"
        )


encuesta()
