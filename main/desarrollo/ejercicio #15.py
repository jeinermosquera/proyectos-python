def factura():
    """Calcula factura con descuento del 8%"""
    print("\n=== EJERCICIO 15: Factura con descuento ===")

    total_venta = 0

    while True:
        articulo = input("Artículo (o 'fin' para terminar): ")
        if articulo.lower() == "fin":
            break

        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio unitario: "))

        subtotal = cantidad * precio
        total_venta += subtotal

    descuento = total_venta * 0.08
    neto_pagar = total_venta - descuento

    print(f"\nTotal venta: ${total_venta:.2f}")
    print(f"Descuento (8%): ${descuento:.2f}")
    print(f"Neto a pagar: ${neto_pagar:.2f}")


factura()
