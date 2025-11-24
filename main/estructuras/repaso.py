
nombres = []
notas = []

def agregar_estudiante(nombre,nota):
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input("Ingrese la nota del estudiante: "))
    nombres.append(nombre)
    notas.append(nota)
    print(f"Estudiante {nombre} con nota {nota} agregado.")

def eliminar_estudiante(nombres,notas):
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre in nombres:
        indice = nombres.index(nombre)
        nombres.pop(indice)
        notas.pop(indice)
        print(f"Estudiante {nombre} eliminado.")
    else:
        print(f"Estudiante {nombre} no encontrado.")

def mostrar_promedio(notas):
    if len(notas) == 0:
        print("No hay notas disponibles para calcular el promedio.")
    else:
        promedio = sum(notas) / len(notas)
        print(f"El promedio de notas es: {promedio}")

def mostrar_estudiantes(nombres,notas):
    print("Lista de estudiantes:")
    if len(nombres) == 0:
        print("No hay estudiantes registrados.")
    else:
        for i in range(len(nombres)):
            print(f"{nombres[i]}: nota {notas[i]}")

def mayor_menor(notas):
    if len(notas) == 0:
        print("No hay notas disponibles para calcular.")
    else:
        mayor = max(notas)
        menor = min(notas)
        print(f"La nota mayor es: {mayor}")
        print(f"La nota menor es: {menor}")

def menu():
    while True:
        print("\n====Gestión de Estudiantes====")
        print("\n1. Agregar estudiante")
        print("2. Eliminar estudiante por nombre")
        print("3. Mostrar todos los estudiantes")
        print("4. Mostrar el promedio de notas")
        print("5. mostrar el mayor y menor promedio")
        print("6. Salir")
        opcion = int(input("Ingrese su opción: "))
    
    
        if opcion == 1:
            agregar_estudiante(nombres,notas)    
        elif opcion == 2:
            eliminar_estudiante(nombres,notas)
        elif opcion == 3:
            mostrar_estudiantes(nombres,notas)
        elif opcion == 4:
            mostrar_promedio(notas)
        elif opcion == 5:
            mayor_menor(notas)
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("opcion no valida")
        
menu()  
