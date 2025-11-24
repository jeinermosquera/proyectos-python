while True:
    try:
        cantidad_vendedores = int(input("Ingrese la cantidad de vendedores: "))
        if cantidad_vendedores <= 0:
            print("Debes de ingresar un numero mayor a 0, intentalo nuevamente.")
        else:
            break
    except ValueError:
        print("Debes de ingresar un numero valido, intentalo nuevamente.")


for vendedor in range(cantidad_vendedores):
    nombre = str(input(f"Ingrese el nombre del vendedor # {vendedor + 1}: "))
    producto = int(
        input(
            f"Ingrese la cantidad de productos que vendio el vendedor # {vendedor + 1}: "
        )
    )
    precio = float(
        input(
            f"Ingrese el valor del producto que vendio el vendedor # {vendedor + 1}: "
        )
    )
    venta_total = producto * precio

    if producto > 50:
        comision = venta_total * 0.1
        print("Exelente.")
    elif producto <= 50 and producto >= 20:
        comision = venta_total * 0.07
        print("Bien.")
    elif producto >= 10 and producto <= 20:
        comision = venta_total * 0.05
        print("Regular.")
    else:
        print("No tienes derechoo a comision.")
        print("Mediocre.")
    print(60 * "=")
