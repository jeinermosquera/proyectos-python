malaria_leve = 0
malaria_grave = 0
malaria_aguda = 0
cancer_leve = 0
cancer_grave = 0
cancer_agudo = 0
tuberculosis_leve = 0
tuberculosis_grave = 0
tuberculosis_aguda = 0
total_pacientes = 0
total_consultas = 0

precio_malaria_leve = 100000
precio_malaria_grave = 150000
precio_malaria_aguda = 200000

precio_cancer_leve = 100000
precio_cancer_grave = 150000
precio_cancer_agudo = 200000

precio_tuberculosis_leve = 100000
precio_tuberculosis_grave = 150000
precio_tuberculosis_aguda = 200000
while True:
    print("Bienvenido a la clinica esperanza.")

    print("Menu de opciones")
    print("1.malaria ")
    print("2. cancer ")
    print("3. tuberculosis ")
    print("4. Salir")

    opcion = input("Seleccione el tipo de consulta que desea realizar: ")

    match opcion:
        case "1":

            print("1. Leve")
            print("2. Grave")
            print("3. Aguda")
            seleccion = int(input("Seleccione el tipo de malaria:"))
            match seleccion:
                case 1:
                    nombre = input("Ingrese su nombre: ")
                    identificacion = input("Ingrese su identificacion: ")
                    print("1. Leve")
                    malaria_leve += 1
                case 2:
                    print("2. Grave")
                    malaria_grave += 1
                    total_consultas += precio_malaria_grave
                case 3:
                    print("3. Aguda")
                    malaria_aguda += 1

                    total_pacientes += 1

        case "2":
            print("1. Leve")
            print("2. Grave")
            print("3. Agudo")
            seleccion = int(input("Seleccione el tipo de cancer:"))
            match seleccion:
                case 1:
                    print("1. Leve")
                    cancer_leve += 1
                case 2:
                    print("2. Grave")
                    cancer_grave += 1
                case 3:
                    print("3. Agudo")
                    cancer_agudo += 1
            nombre = input("Ingrese su nombre: ")
            identificacion = input("Ingrese su identificacion: ")
            total_pacientes += 1

        case "3":

            print("1. Leve")
            print("2. Grave")
            print("3. Agudo")
            seleccion = int(input("Seleccione el tipo de tuberculosis:"))
            match seleccion:
                case 1:
                    print("1. Leve")
                    tuberculosis_leve += 1
                case 2:
                    print("2. Grave")
                    tuberculosis_grave += 1
                case 3:
                    print("3. Agudo")
                    tuberculosis_aguda += 1
            total_pacientes += 1
            nombre = input("Ingrese su nombre: ")
            identificacion = input("Ingrese su identificacion: ")
        case "4":
            print("Saliendo...")
            break
        case _:
            print("Opcion no valida")
print("Resumen de consultas:")
print(f"Total de pacientes atendidos: {total_pacientes}")
print(f"Total de pacientes con malaria leve: {malaria_leve}")
print(f"Total de pacientes con malaria grave: {malaria_grave}")
print(f"Total de pacientes con malaria aguda: {malaria_aguda}")
print(f"Total de pacientes con cancer leve: {cancer_leve}")
print(f"Total de pacientes con cancer grave: {cancer_grave}")
print(f"Total de pacientes con cancer agudo: {cancer_agudo}")
print(f"Total de pacientes con tuberculosis leve: {tuberculosis_leve}")
print(f"Total de pacientes con tuberculosis grave: {tuberculosis_grave}")
print(f"Total de pacientes con tuberculosis aguda: {tuberculosis_aguda}")
print(f"Total de consultas realizadas: {total_consultas}")
