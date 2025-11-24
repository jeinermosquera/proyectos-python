cantidad_vendedores = int(input("\nIngrese la cantidad de vendedores: "))

venta = 0
comision = 0
for vendedor in range(cantidad_vendedores):
    vendedor = str(input(f"Ingrese el nombre del vendedor {vendedor + 1}: "))
    cantidad_productos = int(input("Ingrese la cantida de productos: "))
    precio_producto = float(input(f"ingrese el valor de producto: "))

    venta = cantidad_productos * precio_producto

    if cantidad_productos > 50:
        comision = venta * 0.1
        print("Excelente")
    elif cantidad_productos >= 21 and cantidad_productos <= 50:
        comision = venta * 0.07
        print("Bueno.")
    elif cantidad_productos >= 10 and cantidad_productos <= 20:
        comision = venta * 0.05
        print("Regular.")
    else:
        print("Vendiste muy poco no tienes derecho a una comision.")
        print("Deficiente.")

    print(f"la camtidad de productos que vendidio {vendedor} es: {cantidad_productos}")
    print(f"La comision de {vendedor} es: {comision}")
