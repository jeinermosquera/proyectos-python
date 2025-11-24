def enfermedades():
    """Maneja estadísticas de una clínica especializada"""
    print("\n=== EJERCICIO 24: Clínica especializada ===")

    # Contadores por enfermedad y categoría
    malaria = {"leve": 0, "grave": 0, "aguda": 0}
    cancer = {"leve": 0, "grave": 0, "agudo": 0}
    tuberculosis = {"leve": 0, "grave": 0, "aguda": 0}

    # Valores de consulta por enfermedad y categoría
    precios = {
        "malaria": {"leve": 50000, "grave": 80000, "aguda": 120000},
        "cancer": {"leve": 100000, "grave": 150000, "agudo": 200000},
        "tuberculosis": {"leve": 70000, "grave": 110000, "aguda": 160000},
    }

    recaudado = {
        "malaria": {"leve": 0, "grave": 0, "aguda": 0},
        "cancer": {"leve": 0, "grave": 0, "agudo": 0},
        "tuberculosis": {"leve": 0, "grave": 0, "aguda": 0},
    }

    while True:
        paciente = input("Nombre del paciente (o 'fin' para terminar): ")
        if paciente.lower() == "fin":
            break

        print("Enfermedades: 1=Malaria, 2=Cáncer, 3=Tuberculosis")
        enfermedad_num = int(input("Tipo de enfermedad: "))

        print("Categorías: 1=Leve, 2=Grave, 3=Aguda")
        categoria_num = int(input("Categoría: "))

        # Mapear números a nombres
        enfermedades = {1: "malaria", 2: "cancer", 3: "tuberculosis"}
        categorias_malaria_tb = {1: "leve", 2: "grave", 3: "aguda"}
        categorias_cancer = {1: "leve", 2: "grave", 3: "agudo"}

        enfermedad = enfermedades[enfermedad_num]

        if enfermedad == "cancer":
            categoria = categorias_cancer[categoria_num]
        else:
            categoria = categorias_malaria_tb[categoria_num]

        # Actualizar contadores
        if enfermedad == "malaria":
            malaria[categoria] += 1
        elif enfermedad == "cancer":
            cancer[categoria] += 1
        else:  # tuberculosis
            tuberculosis[categoria] += 1

        # Actualizar recaudación
        precio_consulta = precios[enfermedad][categoria]
        recaudado[enfermedad][categoria] += precio_consulta

        print(
            f"Consulta registrada: {enfermedad.title()} {categoria} - ${precio_consulta}"
        )

    # Mostrar resultados
    total_enfermos = (
        sum(malaria.values()) + sum(cancer.values()) + sum(tuberculosis.values())
    )
    total_recaudado = sum(sum(enf.values()) for enf in recaudado.values())

    print(f"\n=== ESTADÍSTICAS DE LA CLÍNICA ===")
    print(
        f"Malaria leve: {malaria['leve']} pacientes - Recaudado: ${recaudado['malaria']['leve']}"
    )
    print(
        f"Malaria grave: {malaria['grave']} pacientes - Recaudado: ${recaudado['malaria']['grave']}"
    )
    print(
        f"Malaria aguda: {malaria['aguda']} pacientes - Recaudado: ${recaudado['malaria']['aguda']}"
    )
    print(
        f"Cáncer leve: {cancer['leve']} pacientes - Recaudado: ${recaudado['cancer']['leve']}"
    )
    print(
        f"Cáncer grave: {cancer['grave']} pacientes - Recaudado: ${recaudado['cancer']['grave']}"
    )
    print(
        f"Cáncer agudo: {cancer['agudo']} pacientes - Recaudado: ${recaudado['cancer']['agudo']}"
    )
    print(
        f"Tuberculosis leve: {tuberculosis['leve']} pacientes - Recaudado: ${recaudado['tuberculosis']['leve']}"
    )
    print(
        f"Tuberculosis grave: {tuberculosis['grave']} pacientes - Recaudado: ${recaudado['tuberculosis']['grave']}"
    )
    print(
        f"Tuberculosis aguda: {tuberculosis['aguda']} pacientes - Recaudado: ${recaudado['tuberculosis']['aguda']}"
    )
    print(f"\nTotal de enfermos: {total_enfermos}")
    print(f"Total recaudado: ${total_recaudado}")


enfermedades()
