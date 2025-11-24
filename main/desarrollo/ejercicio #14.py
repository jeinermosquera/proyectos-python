def comisiones():
    """Calcula comisiones y pago total de asesores"""
    print("\n=== EJERCICIO 14: Comisiones de ventas ===")

    n = int(input("Número de asesores: "))

    for i in range(n):
        nombre = input(f"Nombre del asesor {i+1}: ")
        sueldo_fijo = float(input(f"Sueldo fijo de {nombre}: "))

        total_ventas = 0
        for j in range(4):
            venta = float(input(f"Venta {j+1}: "))
            total_ventas += venta

        comision = total_ventas * 0.15
        pago_total = sueldo_fijo + comision

        print(f"{nombre}:")
        print(f"  Total ventas: ${total_ventas:.2f}")
        print(f"  Comisión (15%): ${comision:.2f}")
        print(f"  Pago total: ${pago_total:.2f}")


comisiones()
