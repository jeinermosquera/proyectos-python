def venta():
    """Calcula precio de venta con 25% de utilidad"""
    print("\n=== EJERCICIO 21: Precio de venta ===")

    while True:
        articulo = input("Artículo (o 'fin' para terminar): ")
        if articulo.lower() == "fin":
            break

        precio_costo = float(input(f"Precio de costo de {articulo}: "))
        precio_venta = precio_costo * 1.25  # 25% de utilidad

        print(f"{articulo}: Precio de venta: ${precio_venta:.2f}")


venta()
