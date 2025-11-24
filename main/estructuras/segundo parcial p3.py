class Estudiante:
    def __init__(self, nombre, apellido, cedula, edad, nota1, nota2, nota3):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_promedio(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3
    

    def mostrar_informacion(self):
        promedio = self.calcular_promedio()
        print(f"\nCédula: {self.cedula}")
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Nota 1: {self.nota1}")
        print(f"Nota 2: {self.nota2}")
        print(f"Nota 3: {self.nota3}")
        print(f"Promedio: {promedio:.2f}")





estudiantes = []

def agregar_estudiante(nombres,notas):
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    cedula = input("Ingrese la cédula del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    while True:
        try:
            nota1 = float(input("Ingrese la primera nota: "))
            nota2 = float(input("Ingrese la segunda nota: "))
            nota3 = float(input("Ingrese la tercera nota: "))
            if 0 <= nota1 <= 5 and 0 <= nota2 <= 5 and 0 <= nota3 <= 5:
                break
            else:
                print("Las notas deben estar entre 0 y 5. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido para las notas.")

    estudiante1 = Estudiante(nombre, apellido, cedula, edad, nota1, nota2, nota3)
    estudiantes.append(estudiante1)
    print("Estudiante agregado con éxito.")

def mostrar_todo_estudiante( ):
    if not estudiantes:
        print("\nNo hay estudiantes registrados.")
        return
    
    print("\n--- Lista de Estudiantes ---")
    for est in estudiantes:
        est.mostrar_informacion()

def buscar_estudiante():
    cedula = input("\nIngrese la cédula del estudiante: ")
    for est in estudiantes:
        if est.cedula == cedula:
            est.mostrar_informacion()
            return
    print("Estudiante no encontrado.")


def eliminar_estudiante_cedula():
    cedula = input("Ingrese la cédula del estudiante a eliminar: ")
    for estudiante in estudiantes:
        if estudiante.cedula == cedula:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado con éxito.")
            return
    print("Cédula no encontrada.")


def mejor_promedio_y_peor_promedio():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    mejor = [estudiantes[0]]
    peor = [estudiantes[0]]
    for estudiante in estudiantes[1:]:
        if estudiante.calcular_promedio() > mejor[0].calcular_promedio():
            mejor = [estudiante]
        elif estudiante.calcular_promedio() == mejor[0].calcular_promedio():
            mejor.append(estudiante)
        if estudiante.calcular_promedio() < peor[0].calcular_promedio():
            peor = [estudiante]
        elif estudiante.calcular_promedio() == peor[0].calcular_promedio():
            peor.append(estudiante)
    print("Estudiante(s) con el mejor promedio:")
    for estudiante in mejor:
        print(estudiante.mostrar_informacion())
    print("Estudiante(s) con el peor promedio:")
    for estudiante in peor:
        print(estudiante.mostrar_informacion())

def menu():
    while True:
        print("\n====Gestión de Estudiantes====")
        print("1. Agregar estudiante")
        print("2. Mostrar información del estudiante")
        print("3. Buscar estudiante")
        print("4. Eliminar estudiante")
        print("5. Mejor y peor promedio")
        print("6. Salir")
        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            nombre = input("Ingrese el nombre del estudiante: ")
            apellido = input("Ingrese el apellido del estudiante: ")
            cedula = input("Ingrese la cédula del estudiante: ")
            edad = int(input("Ingrese la edad del estudiante: "))
            nota1 = float(input("Ingrese la primera nota: "))
            nota2 = float(input("Ingrese la segunda nota: "))
            nota3 = float(input("Ingrese la tercera nota: "))
            estudiante1 = Estudiante(nombre, apellido, cedula, edad, nota1, nota2, nota3)
            print("Estudiante agregado con éxito.")
            estudiantes.append(estudiante1)
        elif opcion == 2:
            mostrar_todo_estudiante()
        elif opcion == 3:
            buscar_estudiante()
        elif opcion == 4:
            eliminar_estudiante_cedula()
        elif opcion == 5:
            mejor_promedio_y_peor_promedio()

        elif opcion == 6:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()