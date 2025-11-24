numero_pacientes = 0
malaria_leve = 0
malaria_grave = 0
malaria_aguda = 0
cancer_leve = 0
cancer_grave = 0
cancer_agudo = 0
tuberculosis_leve = 0
tuberculosis_grave = 0
tuberculosis_agudo = 0
total_consultas = 0

precio_malaria_leve = 100
precio_malaria_grave = 200
precio_malaria_aguda = 300
precio_cancer_leve = 150
precio_cancer_grave = 250
precio_cancer_agudo = 350
precio_tuberculosis_leve = 120
precio_tuberculosis_grave = 220
precio_tuberculosis_agudo = 320

while True:

    print("Bienvenido a la clinica esperanza.")

    print("menu de consultas")
    print("1. Malaria")
    print("2. Cancer")
    print("3. Tuberculosis")
    print("4. Salir")

    opcion = int(input("Seleccione el tipo de consulta que desea realizar: "))

    match opcion:
        case 1:
            print(60 * "=")
            print("Ha seleccionado Malaria")
            print("Seleccione el tipo de malaria:")
            print(f"1. Leve, precio {precio_malaria_leve} $")
            print(f"2. Grave, precio {precio_malaria_grave} $")
            print(f"3. Aguda, precio {precio_malaria_aguda} $")
            eleccion = int(input("Seleccione el tipo de malaria:"))
            nombre = input("Ingrese su nombre: ")
            print("Registro terminado.")
            print(60 * "=")

            match eleccion:
                case 1:
                    numero_pacientes += 1
                    malaria_leve += 1
                    total_consultas += precio_malaria_leve
                case 2:
                    numero_pacientes += 1
                    malaria_grave += 1
                    total_consultas += precio_malaria_grave
                case 3:
                    numero_pacientes += 1
                    malaria_aguda += 1
                    total_consultas += precio_malaria_aguda

        case 2:
            print(60 * "=")
            print("Ha seleccionado Cancer")
            print("Seleccione el tipo de cancer:")
            print(f"1. Leve, precio {precio_cancer_leve} $")
            print(f"2. Grave, precio {precio_cancer_grave} $")
            print(f"3. Agudo, precio {precio_cancer_agudo} $")
            eleccion = int(input("Seleccione el tipo de cancer:"))
            nombre = input("Ingrese su nombre: ")
            print("Registro terminado.")
            print(60 * "=")

            match eleccion:
                case 1:
                    numero_pacientes += 1
                    cancer_leve += 1
                    total_consultas += precio_cancer_leve
                case 2:
                    numero_pacientes += 1
                    cancer_grave += 1
                    total_consultas += precio_cancer_grave
                case 3:
                    numero_pacientes += 1
                    cancer_agudo += 1
                    total_consultas += precio_cancer_agudo

        case 3:
            print(60 * "=")
            print("Ha seleccionado Tuberculosis")
            print(f"1. Leve, precio {precio_tuberculosis_leve} $")
            print(f"2. Grave, precio {precio_tuberculosis_grave} $")
            print(f"3. Agudo, precio {precio_tuberculosis_agudo} $")
            eleccion = int(input("Seleccione el tipo de tuberculosis:"))
            nombre = input("Ingrese su nombre: ")
            print("Registro terminado.")
            print(60 * "=")

            match eleccion:
                case 1:
                    numero_pacientes += 1
                    tuberculosis_leve += 1
                    total_consultas += precio_tuberculosis_leve
                case 2:
                    numero_pacientes += 1
                    tuberculosis_grave += 1
                    total_consultas += precio_tuberculosis_grave
                case 3:
                    numero_pacientes += 1
                    tuberculosis_agudo += 1
                    total_consultas += precio_tuberculosis_agudo
        case 4:
            print("programa finalizado...")
            break
        case _:
            print("Opcion no valida")
print(60 * "=")
print("Resumen de consultas:")
print(f"Total de pacientes atendidos: {numero_pacientes}.")
print(f"Malaria leve: {malaria_leve}.")
print(f"Malaria aguda: {malaria_aguda}.")
print(f"Malaria grave: {malaria_grave}.")
print(f"Cancer leve: {cancer_leve}.")
print(f"Cancer grave: {cancer_grave}.")
print(f"Cancer agudo: {cancer_agudo}.")
print(f"Tuberculosis leve: {tuberculosis_leve}.")
print(f"Tuberculosis grave: {tuberculosis_grave}.")
print(f"Tuberculosis agudo: {tuberculosis_agudo}.")
print(f"Total de consultas: {total_consultas} $.")
