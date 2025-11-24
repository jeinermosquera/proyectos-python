while True:
    try:
        estudiantes = int(input("Ingrese el número de estudiantes: "))
        if estudiantes <= 0:
            raise ValueError("El número de estudiantes debe ser mayor que cero.")
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero positivo.")

edades = []
for i in range(estudiantes):
    while True:
        try:
            edad = int(input(f"Ingrese la edad del estudiante # {i + 1}: "))
            edades.append(edad)
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    total_edad = sum(edades)
    promedio_edad = total_edad / len(edades)

print(f"La edad promedio de los estudiantes es: {promedio_edad} años.")
