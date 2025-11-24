estudiantes = 0
contador_saludable = 0
contador1_no_saludable = 0


estudiantes = int(input("\nIngrese el numero de estudiates:"))
for estudiante in range(estudiantes):
    horas = int(
        input(
            f"\ningresa cuantas horas dueremes cada dia el estudiate {estudiante + 1}: "
        )
    )
    actividad = int(input("cuantas veces a la semana realizas actividades fisicas: "))
    frutas = int(input("Cuantas porciones de frutas y verduras comes al dia: "))

    if horas >= 7 and actividad >= 3 and frutas >= 5:
        print("tienes un estilo de vida saludable.")
        contador_saludable += 1
    else:
        print("No tienes vida saludable")
        contador1_no_saludable += 1


porcentaje_saludable = contador_saludable * 100 / estudiantes
print(40 * "=")
print(f"\nlos estudiantes con vida saludable son: {contador_saludable}")
print(f"los estudiantes no saludables son: {contador1_no_saludable}")
print(f"el porcentaje de estudiates saludables son: {porcentaje_saludable}%")
print(f"El total de estudiantes son:{estudiantes}")

if porcentaje_saludable >= 70:
    print("buen estado de salud en general.")
elif porcentaje_saludable >= 40:
    print("nivel aceptable, pero puede mejorar.")
else:
    print("alerta roja, se requieres campañas urgentes.")
