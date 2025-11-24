def datos_usuario():
    print("\n====Ingrese sus datos personales====")
    nombre = input("\nIngrese su nombre completo: ")
    identificacion = int(input("Ingrese su número de identificación: "))


def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    if imc < 18:
        print("Tu estas por debajo del peso ideal")
    elif 18 <= imc <= 25:
        print("Tu tienes un peso ideal")
    else:
        print("Tu tienes sobrepeso")


def es_mayor_de_edad(edad):
    if edad >= 18:
        print("Tu eres mayor de edad")
    else:
        print("Tu eres menor de edad")


def sexo_valido(sexo):
    if sexo == 1:
        print("Sexo masculino")
    elif sexo == 2:
        print("Sexo femenino")
    else:
        print("Sexo no válido")


def DNI():
    import random

    DNI = random.sample(range(0, 10), 8)
    DNI = int("".join(map(str, DNI)))
    return DNI


def menu():
    print("====menú====")
    print("\n1. Calcular IMC")
    print("2. Verificar mayoría de edad")
    print("3. Verificar sexo válido")
    print("4. Generar DNI")
    print("5. Salir")
    opcion = int(input("ingrese la opción que desea ver: "))
    return opcion


def mostrar_informacion():
    while True:
        datos_usuario()
        opcion = menu()

        match opcion:
            case 1:
                peso = float(input("Ingrese su peso en kg: "))
                altura = float(input("Ingrese su altura en centimetros: "))
                calcular_imc(peso, altura)
            case 2:
                edad = int(input("Ingrese su edad: "))
                es_mayor_de_edad(edad)
            case 3:
                sexo = int(input("Ingrese su sexo (1:M/ 2:F): "))
                sexo_valido(sexo)
            case 4:

                dni = DNI()
                print(f"tu DNI es:{dni}")
            case 5:
                continuar = input("¿Desea continuar? (1:s/2:n): ")
                if continuar != "1":
                    break


mostrar_informacion()
