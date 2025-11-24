class Estudiante:
    def _init_(self, cedula, nombre, apellido, edad, nota1, nota2, nota3):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
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


# Lista para almacenar estudiantes
estudiantes = []


def agregar_estudiante():
    print("\n--- Agregar Estudiante ---")
    cedula = input("Cédula: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    
    estudiante = Estudiante(cedula, nombre, apellido, edad, nota1, nota2, nota3)
    estudiantes.append(estudiante)
    print("Estudiante agregado exitosamente.")


def mostrar_todos():
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


def eliminar_estudiante():
    cedula = input("\nIngrese la cédula del estudiante a eliminar: ")
    for i, est in enumerate(estudiantes):
        if est.cedula == cedula:
            estudiantes.pop(i)
            print("Estudiante eliminado exitosamente.")
            return
    print("Estudiante no encontrado.")


def mostrar_mejor_promedio():
    if not estudiantes:
        print("\nNo hay estudiantes registrados.")
        return
    
    mejor = max(estudiantes, key=lambda e: e.calcular_promedio())
    peor = min(estudiantes, key=lambda e: e.calcular_promedio())
    
    print("\n--- Estudiante con Mejor Promedio ---")
    mejor.mostrar_informacion()
    
    print("\n--- Estudiante con Peor Promedio ---")
    peor.mostrar_informacion()


def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("[1] Agregar estudiante")
        print("[2] Mostrar todos")
        print("[3] Buscar estudiante")
        print("[4] Eliminar estudiante")
        print("[5] Mostrar mejor promedio")
        print("[6] Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            mostrar_todos()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            mostrar_mejor_promedio()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecutar el programa
if __name__ == "__main__":
    menu()