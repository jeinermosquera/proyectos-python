def mostrar_menu():
    print("\n" + "=" * 40)
    print("MENÚ DE OPERACIONES GEOMÉTRICAS")
    print("=" * 40)
    print("[1] Área del rectángulo")
    print("[2] Área del triángulo")
    print("[3] Área del círculo")
    print("[4] Perímetro del rectángulo")
    print("[5] Perímetro del triángulo")
    print("[6] Circunferencia del círculo")
    print("[7] Salir del programa")
    print("=" * 40)
    print("Seleccione una opción (1-7): ")
    return input("Opción: ")


def area_rectangulo(base, altura):
    return base * altura


def area_triangulo(base, altura):
    return (base * altura) / 2


def area_circulo(radio):
    import math

    return math.pi * radio**2


def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)


def perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3


def circunferencia_circulo(radio):
    import math

    return 2 * math.pi * radio


def resultado():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            print(f"Área del rectángulo: {area_rectangulo(base, altura)}")
        elif opcion == "2":
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            print(f"Área del triángulo: {area_triangulo(base, altura)}")
        elif opcion == "3":
            radio = float(input("Ingrese el radio del círculo: "))
            print(f"Área del círculo: {area_circulo(radio)}")
        elif opcion == "4":
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            print(f"Perímetro del rectángulo: {perimetro_rectangulo(base, altura)}")
        elif opcion == "5":
            lado1 = float(input("Ingrese el primer lado del triángulo: "))
            lado2 = float(input("Ingrese el segundo lado del triángulo: "))
            lado3 = float(input("Ingrese el tercer lado del triángulo: "))
            print(
                f"Perímetro del triángulo: {perimetro_triangulo(lado1, lado2, lado3)}"
            )
        elif opcion == "6":
            radio = float(input("Ingrese el radio del círculo: "))
            print(f"Circunferencia del círculo: {circunferencia_circulo(radio)}")
        elif opcion == "7":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


resultado()
