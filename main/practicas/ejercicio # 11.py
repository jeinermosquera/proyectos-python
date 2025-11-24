def calcular_nota(nota1, nota2, nota3):
    return nota1 * 0.3 + nota2 * 0.3 + nota3 * 0.4


def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")


def main():
    estudiantes = {}
    cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
    for i in range(1, cantidad_estudiantes + 1):
        print(f"\nEstudiante #{i}")
        nombre = input("Ingrese el nombre del estudiante: ")
        nota1 = pedir_float("Ingrese la nota #1: ")
        nota2 = pedir_float("Ingrese la nota #2: ")
        nota3 = pedir_float("Ingrese la nota #3: ")
        promedio = calcular_nota(nota1, nota2, nota3)
        estudiantes[nombre] = promedio

    print("\nResultados:")
    for nombre, promedio in estudiantes.items():
        print(f"El promedio de {nombre} es: {promedio:.2f}")
