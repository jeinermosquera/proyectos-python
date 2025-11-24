def factura():
    """Calcula facturación con IVA para varios artículos"""
    print("\n=== EJERCICIO 8: Facturación con IVA ===")

    iva_porcentaje = float(input("Porcentaje de IVA: ")) / 100
    total_sin_iva = 0
    total_iva = 0

    while True:
        articulo = input("Nombre del artículo (o 'fin' para terminar): ")
        if articulo.lower() == "fin":
            break

        cantidad = int(input("Cantidad: "))
        precio_unitario = float(input("Precio unitario: "))

        subtotal = cantidad * precio_unitario
        iva_articulo = subtotal * iva_porcentaje
        total_articulo = subtotal + iva_articulo

        print(f"{articulo}:")
        print(f"  Valor sin IVA: ${subtotal:.2f}")
        print(f"  IVA: ${iva_articulo:.2f}")
        print(f"  Total: ${total_articulo:.2f}")

        total_sin_iva += subtotal
        total_iva += iva_articulo

    print(f"\nResumen de la factura:")
    print(f"Total sin IVA: ${total_sin_iva:.2f}")
    print(f"Total IVA: ${total_iva:.2f}")
    print(f"Total con IVA: ${total_sin_iva + total_iva:.2f}")


factura()
