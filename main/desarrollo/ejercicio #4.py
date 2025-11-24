def descuento():
    """Descuento del 20% para deudas > 6000000 con facilidad de 6 cuotas"""
    print("\n=== EJERCICIO 4: Descuento bancario ===")

    n = int(input("Número de deudores: "))

    for i in range(n):
        nombre = input(f"Nombre del deudor {i+1}: ")
        deuda = float(input(f"Monto de la deuda de {nombre}: "))

        if deuda > 6000000:
            descuento = deuda * 0.20
            deuda_con_descuento = deuda - descuento
            cuota_mensual = deuda_con_descuento / 6

            print(f"{nombre}:")
            print(f"  Deuda sin descuento: ${deuda:.2f}")
            print(f"  Descuento (20%): ${descuento:.2f}")
            print(f"  Deuda con descuento: ${deuda_con_descuento:.2f}")
            print(f"  Cuota mensual (6 cuotas): ${cuota_mensual:.2f}")
        else:
            print(f"{nombre}: Deuda de ${deuda:.2f} - No aplica para descuento")


descuento()
