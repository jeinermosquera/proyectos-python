def promedio():
    """Calcula promedio de notas de estudiantes"""
    print("\n=== EJERCICIO 11: Notas de estudiantes ===")

    estudiantes = []
    suma_promedios = 0

    while True:
        nombre = input("Nombre del estudiante (o 'fin' para terminar): ")
        if nombre.lower() == "fin":
            break

        nota1 = float(input("Primera nota: "))
        nota2 = float(input("Segunda nota: "))
        nota3 = float(input("Tercera nota: "))

        promedio = (nota1 + nota2 + nota3) / 3

        estudiante = {
            "nombre": nombre,
            "nota1": nota1,
            "nota2": nota2,
            "nota3": nota3,
            "promedio": promedio,
        }

        estudiantes.append(estudiante)
        suma_promedios += promedio

        print(f"{nombre}: Notas: {nota1}, {nota2}, {nota3} - Promedio: {promedio:.2f}")

    if estudiantes:
        promedio_general = suma_promedios / len(estudiantes)
        print(f"\nTotal de estudiantes: {len(estudiantes)}")
        print(f"Promedio general: {promedio_general:.2f}")


promedio()
