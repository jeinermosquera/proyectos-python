def calcular_comision(cantidad, venta_total):
    if cantidad > 50:
        print("Excelente")
        return venta_total * 0.1
    elif 21 <= cantidad <= 50:
        print("Bueno.")
        return venta_total * 0.07
    elif 10 <= cantidad <= 20:
        print("Regular.")
        return venta_total * 0.05
    else:
        print("Vendiste muy poco, no tienes derecho a una comisión.")
        print("Deficiente.")
        return 0


def procesar_vendedor(numero_vendedor):
    nombre = input(f"Ingrese el nombre del vendedor {numero_vendedor}: ")
    cantidad = int(
        input(
            f"Ingrese la cantidad vendida del producto por el vendedor #{numero_vendedor}: "
        )
    )
    precio_unitario = float(input("Ingrese el precio unitario del producto: "))
    venta_total = cantidad * precio_unitario

    comision = calcular_comision(cantidad, venta_total)
    print(f"La cantidad de productos que vendió {nombre} es: {cantidad}")
    print(f"La comisión de {nombre} es: {comision}")


def main():
    cantidad_vendedores = int(input("Ingrese la cantidad de vendedores: "))
    for i in range(1, cantidad_vendedores + 1):
        procesar_vendedor(i)


if __name__ == "__main__":
    main()
