while True:
    print("-----------------Menu de opciones-------------------------")
    print("")
    print("1. Area del rectangulo")
    print("2. Area del triangulo")
    print("3. Area del circulo")
    print("4. Perimetro del cuadrado")
    print("5. Perimetro del triangulo")
    print("6. Perimetro del circulo")
    print("7. Salir")
    print(40 * "-")

    opcion = input("Seleccione la opcion que desea realizar: ")

    if opcion == "1":
        altura = float(input("ingrese la altura del rectangulo: "))
        base = float(input("ingrese la base del rectangulo: "))
        area = base * altura
        print("El area del rectangulo es: ", area)

    elif opcion == "2":
        base = float(input("ingrese la base del triangulo: "))
        altura = float(input("ingrese la altura del triangulo: "))
        area = (base * altura) / 2
        print("El area del triangulo es: ", area)

    elif opcion == "3":
        radio = float(input("ingrese el radio del circulo: "))
        area = 3.1416 * radio**2
        print("El area del circulo es: ", area)

    elif opcion == "4":
        altura = float(input("ingrese la altura del rectangulo: "))
        base = float(input("ingrese la base del rectangulo: "))
        perimetro = 2 * (base + altura)
        print("El perimetro del rectangulo es: ", perimetro)

    elif opcion == "5":
        lado1 = float(input("ingrese el lado 1 del triangulo: "))
        lado2 = float(input("ingrese el lado 2 del triangulo: "))
        lado3 = float(input("ingrese el lado 3 del triangulo: "))
        perimetro = lado1 + lado2 + lado3
        print("El perimetro del triangulo es: ", perimetro)

    elif opcion == "6":
        radio = float(input("ingrese el radio del circulo: "))
        perimetro = 2 * 3.1416 * radio
        print("El perimetro del circulo es: ", perimetro)

    elif opcion == "7":
        print("Saliendo...")
        salir = input("¿Está seguro que desea salir? (s/n): ")
        if salir == "s":
            break
    else:
        print("Opcion no valida")
