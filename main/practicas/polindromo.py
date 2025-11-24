saldos = {"andres": 200000, "camilo": 150000, "juan": 300000, "jose": 50000}
while True:
    print(60 * "-")
    print("\nBienvenido al cajero.")
    print("\n1. Retirar dinero")
    print("2. Consultar saldo")
    print("3. Consignar dinero")
    print("4. Salir")

    opcion = int(input("\nSeleccione una opción: "))
    match opcion:
        case 1:
            nombre = input("Ingrese su nombre: ")
            nombre = nombre.lower()
            saldo = saldos.get(nombre, 0)
            retiro = float(
                input(f"su saldo es de {saldo} $ \nIngrese el monto a retirar: ")
            )
            if retiro > saldo:
                print("Fondos insuficientes.")
            else:
                saldo -= retiro
                saldos[nombre] = saldo
                print(f"Retiro exitoso. Tu nuevo saldo es: {saldo} $")
        case 2:
            nombre = input("Ingrese su nombre: ")
            nombre = nombre.lower()
            saldo = saldos.get(nombre, 0)
            print(f"Tu saldo es: {saldo} $")
        case 3:
            nombre = input("Ingrese su nombre: ")
            nombre = nombre.lower()
            saldo = saldos.get(nombre, 0)
            consignar = float(
                input(f"su saldo es de {saldo} $ \nIngrese el monto a consignar: ")
            )
            saldo += consignar
            saldos[nombre] = saldo
            print(f"Consignación exitosa. Tu nuevo saldo es: {saldo} $")
        case 4:
            print("Gracias por utilizar el cajero.")
            break
        case _:
            print("Opción inválida. Por favor, seleccione una opción válida.")
