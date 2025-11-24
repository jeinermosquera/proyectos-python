while True:
    print(15 * " ", "Menu de opciones")
    print(" ")
    print("1. Area del rectangulo")
    print("2. Area del triangulo")
    print("3. Area del circulo")
    print("4. Perimetro del cuadrado")
    print("5. Perimetro del triangulo")
    print("6. Perimetro del circulo")
    print("7. Salir")

    print(40 * "-")

    opcion = int(input("Seleccione la opcion que desea realizar: "))

    match opcion:
        case 1:
            altura = float(input("ingrese la altura del rectangulo: "))
            base = float(input("ingrese la base del rectangulo: "))
            area = base * altura
            print("El area del rectangulo es: ", area)

        case 2:
            base = float(input("ingrese la base del triangulo: "))
            altura = float(input("ingrese la altura del triangulo: "))
            area = (base * altura) / 2
            print("El area del triangulo es: ", area)

        case 3:
            radio = float(input("ingrese el radio del circulo: "))
            area = 3.1416 * radio**2
            print("El area del circulo es: ", area)

        case 4:
            altura = float(input("ingrese la altura del rectangulo: "))
            base = float(input("ingrese la base del rectangulo: "))
            perimetro = 2 * (base + altura)
            print("El perimetro del rectangulo es: ", perimetro)

        case 5:
            lado1 = float(input("ingrese el lado 1 del triangulo: "))
            lado2 = float(input("ingrese el lado 2 del triangulo: "))
            lado3 = float(input("ingrese el lado 3 del triangulo: "))
            perimetro = lado1 + lado2 + lado3
            print("El perimetro del triangulo es: ", perimetro)

        case 6:
            radio = float(input("ingrese el radio del circulo: "))
            perimetro = 2 * 3.1416 * radio
            print("El perimetro del circulo es: ", perimetro)

        case 7:
            salir = input("¿Está seguro que desea salir? (s/n): ")
            if salir == "s":
                print("Saliendo...")
                break
        case _:
            print("Opcion no valida")
