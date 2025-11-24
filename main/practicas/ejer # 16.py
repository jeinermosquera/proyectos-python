deuda_total = 0
descuento = 0
cuotas = 0
while True:
    nombre = input("Ingrese el nombre del deudor: ")
    deuda = float(input("Ingrese el monto de la deuda: "))
    if deuda > 6000000:
        deuda_total = deuda * 0.2
        descuento = deuda - deuda_total
        cuotas = deuda_total / 6
    else:
        print(f"No tiene derecho a un descuento por que tu deuda es de {deuda}.")
    print(40 * "-")
    print(f"El nombre del deudor es: {nombre}")
    print(f"La deuda antes del descuento es de: {deuda} $")
    print(f"El monto total a pagar es de: {descuento} $")
    print(f"La deuda despues del descuento es de: {deuda_total} $")
    print(f"El monto de cada cuota mensual es de: {cuotas} $")

    continuar = int(input("¿Desea ingresar otra deuda? s(1)/n(2): "))
    if continuar == 2:
        print("su proceso ha finalizado con éxito...")
        break
