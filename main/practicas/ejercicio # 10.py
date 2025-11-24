while True:
    print("Bienvenido a la calculadora de figuras geométricas.")
    print("1. Círculo")
    print("2. Cuadrado")
    print("3. Triángulo")
    print("4. Salir")
    opcion = int(input("Ingrese el número de la opción deseada: "))

    match opcion:
        case 1:
            radio = float(input("Ingrese el radio del círculo: "))
            area = 3.14159 * radio**2
            print(f"El área del círculo es: {area}")
        case 2:
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = lado**2
            print(f"El área del cuadrado es: {area}")
        case 3:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = 0.5 * base * altura
            print(f"El área del triángulo es: {area}")
        case 4:
            salir = int(input("¿Está seguro que desea salir? (1: sí / 0: no): "))
            if salir == 1:
                print("Saliendo de la calculadora.")
                break
