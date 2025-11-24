def nota_final():
    """Calcula nota final con porcentajes específicos"""
    print("\n=== EJERCICIO 16: Nota final ===")

    n = int(input("Número de estudiantes: "))

    for i in range(n):
        nombre = input(f"Nombre del estudiante {i+1}: ")
        nota1 = float(input("Primera nota (30%): "))
        nota2 = float(input("Segunda nota (30%): "))
        nota3 = float(input("Tercera nota (40%): "))

        nota_final = (nota1 * 0.30) + (nota2 * 0.30) + (nota3 * 0.40)

        print(f"{nombre}: Nota final: {nota_final:.2f}")


nota_final()
