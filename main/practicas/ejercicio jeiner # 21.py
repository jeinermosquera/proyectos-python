cantida_estudiantes = int(input("Ingrese la cantidad de estudiantes a matricular: "))

valor_materia = 200000
total_matricula = 0
estudiante_civil = 0
estudiante_telecomunicaciones = 0
estudiante_ambiental = 0
materias_telecomunicaciones = 0
materias_civil = 0
materias_ambiental = 0
promedio_materia_telecomunicaciones = 0
promedio_materia_civil = 0
promedio_materia_ambiental = 0
num_estudiantes = 0
total_matricula_piti = 0
total_matricula_civil = 0
total_matricula_ambiental = 0


for estudiante in range(cantida_estudiantes):
    nombre = str(input(f"Ingrese el nombre del estudiante # {estudiante + 1}: "))

    print("carreras disponibles")
    print("1.ingenieria en telecomunicaciones e informatica")
    print("2.ingenieria civil")
    print("3.ingenieria ambiental")

    carrera = int(
        input(f"Ingrese el numero de la carrera del estudiante # {estudiante + 1}: ")
    )
    match carrera:
        case 1:
            estudiante_telecomunicaciones += 1
            while True:
                becado = int(
                    input(
                        f"el estudiante # {estudiante + 1} es becado. 1.(si) / 2.(no): "
                    )
                )
                num_materias = int(
                    input(
                        f"Ingrese el numero de materias que desea matricular el estudiante {estudiante + 1} no deben ser mas de 8: "
                    )
                )

                if becado == 1:
                    if num_materias > 8:
                        print("No debes matricular mas de 8 materias.")
                    elif num_materias <= 8:
                        materias_telecomunicaciones += num_materias
                        total_matricula_piti = num_materias * valor_materia
                        total_matricula_piti = total_matricula_piti * 0.85
                        total_matricula += total_matricula_piti

                        break
                elif becado == 2:
                    if num_materias > 8:
                        print("No debes matricular mas de 8 materias.")
                    elif num_materias <= 8:
                        materias_telecomunicaciones += num_materias
                        total_matricula_piti = num_materias * valor_materia
                        total_matricula += total_matricula_piti
                        break

        case 2:
            estudiante_civil += 1
            while True:
                becado = int(
                    input(
                        f"el estudiante # {estudiante + 1} es becado. 1.(si) / 2.(no): "
                    )
                )
                num_materias = int(
                    input(
                        f"Ingrese el numero de materias que desea matricular el estudiante {estudiante + 1} no deben ser mas de 8: "
                    )
                )
                if becado == 1:
                    if num_materias > 8:
                        print("No debes matricular mas de 8 materias.")
                    elif num_materias <= 8:
                        materias_civil += num_materias
                        total_matricula_civil = num_materias * valor_materia
                        total_matricula_civil = total_matricula_civil * 0.85
                        total_matricula += total_matricula_civil
                        break
                elif becado == 2:
                    if num_materias > 8:
                        print("No debes matricular mas de 8 materias.")
                    elif num_materias <= 8:
                        materias_civil += num_materias
                        total_matricula_civil = num_materias * valor_materia
                        total_matricula += total_matricula_civil
                        break

        case 3:
            estudiante_ambiental += 1
            while True:

                becado = int(
                    input(
                        f"el estudiante # {estudiante + 1} es becado. 1.(si) / 2.(no): "
                    )
                )
                num_materias = int(
                    input(
                        f"Ingrese el numero de materias que desea matricular el estudiante {estudiante + 1} no deben ser mas de 8: "
                    )
                )
                if becado == 1:
                    if num_materias > 8:
                        print("No debes matricular mas de 8 materias.")
                    elif num_materias <= 8:
                        materias_ambiental += num_materias
                        total_matricula_ambiental = num_materias * valor_materia
                        total_matricula_ambiental = total_matricula_ambiental * 0.85
                        total_matricula += total_matricula_ambiental
                        break
                elif becado == 2:
                    if num_materias > 8:
                        print("No debes matricular mas de 8 materias.")
                    elif num_materias <= 8:
                        materias_ambiental += num_materias
                        total_matricula_ambiental = num_materias * valor_materia
                        total_matricula += total_matricula_ambiental
                        break

num_estudiantes = (
    estudiante_telecomunicaciones + estudiante_civil + estudiante_ambiental
)

print(40 * "-")
if materias_telecomunicaciones > 0 and estudiante_telecomunicaciones > 0:
    promedio_materia_telecomunicaciones = (
        materias_telecomunicaciones / estudiante_telecomunicaciones
    )
    print(
        f"el promedio de materias de ingenieria de telecomunicaciones es {promedio_materia_telecomunicaciones}"
    )

else:
    print("el promedio de materias de ingenieria en telecomunicaciones es cero.")

if materias_civil > 0 and estudiante_civil > 0:
    promedio_materia_civil = materias_civil / estudiante_civil
    print(f"el promedio de ingenieria civil es {promedio_materia_civil}")

else:
    print("El promedio de ingenieria civil es cero.")


if materias_ambiental > 0 and estudiante_ambiental > 0:
    promedio_materia_ambiental = materias_ambiental / estudiante_ambiental
    print(f"el promedio de materias ambiental es {promedio_materia_ambiental}")

else:
    print("El numero de estudiantes de ingenira ambiental es cero.")


if (
    estudiante_telecomunicaciones > estudiante_civil
    and estudiante_telecomunicaciones > estudiante_ambiental
):
    print(
        f"La carrera con mas estudiantes es telecomunicaciones con # {estudiante_telecomunicaciones} estudiantes."
    )
elif (
    estudiante_civil > estudiante_telecomunicaciones
    and estudiante_civil > estudiante_ambiental
):
    print(
        f"La carrera con mas estudiantes es civil con # {estudiante_civil} estudiantes."
    )
elif (
    estudiante_ambiental > estudiante_telecomunicaciones
    and estudiante_ambiental > estudiante_civil
):
    print(
        f"La carrera con mas estudiantes es ambiental con # {estudiante_ambiental} estudiantes."
    )


print(f"El total recadudado fueron: {total_matricula} $")

if estudiante_telecomunicaciones < 5:
    print(
        "Alerta la carrera de ingenieria de telecomunicaciones e informatica tiene muy pocos estudiantes."
    )
if estudiante_civil < 5:
    print("Alerta la carrera de ingenieria civil tiene muy pocos estudiantes.")

if estudiante_ambiental < 5:
    print("Alerta la carrera de ingenieria ambiental tiene muy pocos estudiantes.")
