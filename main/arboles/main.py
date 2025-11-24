import arboles

inventario = arboles.SistemaInventario()

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("SISTEMA DE INVENTARIO")
    print("="*50)
    print("1. Agregar producto(s)")
    print("2. Buscar producto por código")
    print("3. Listar todos los productos")
    print("4. Buscar por rango de precio")
    print("5. Actualizar stock")
    print("6. Ver estructura del árbol (gráfico)")
    print("7. Cargar 10 productos de prueba")
    print("8. Salir")
    print("="*50)

def cargar_productos_prueba(inventario):
    """Carga 10 productos de prueba en el inventario"""
    productos_prueba = [
        (50, "Laptop", 1200.00, 15),
        (30, "Mouse", 25.50, 50),
        (70, "Monitor", 350.00, 20),
        (20, "Teclado", 45.00, 30),
        (40, "Webcam", 80.00, 25),
        (60, "Auriculares", 65.00, 40),
        (80, "Impresora", 200.00, 10),
        (10, "Cable HDMI", 15.00, 100),
        (35, "Hub USB", 30.00, 35),
        (75, "Micrófono", 120.00, 18)
    ]
    
    print("\n" + "="*50)
    print("CARGANDO 10 PRODUCTOS DE PRUEBA...")
    print("="*50)
    
    for codigo, nombre, precio, stock in productos_prueba:
        inventario.agregar_producto(codigo, nombre, precio, stock)
    
    print(f"\n{'='*50}")
    print(f"✓ Se cargaron {len(productos_prueba)} productos exitosamente")
    print(f"{'='*50}")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    
    match opcion:
        case "1":
            # Agregar producto(s)
            print("\n--- AGREGAR PRODUCTO(S) ---")
            
            while True:
                try:
                    cantidad = int(input("¿Cuántos productos desea agregar? "))
                    if cantidad > 0:
                        break
                    print("✗ Debe agregar al menos 1 producto.")
                except ValueError:
                    print("✗ Debe ingresar un número válido. Intente de nuevo.")
            
            productos_agregados = 0
            
            for i in range(cantidad):
                print(f"\n{'='*50}")
                print(f"PRODUCTO {i+1} DE {cantidad} ({cantidad - i} restantes)")
                print(f"{'='*50}")
                
                while True:
                    try:
                        codigo = int(input(f"Ingrese el CÓDIGO del producto {i+1}: "))
                        if inventario.buscar_producto(codigo):
                            print(f"✗ Este código ya existe. Ingrese uno diferente para el producto {i+1}.")
                            continue
                        break
                    except ValueError:
                        print(f"✗ Error: No puede ingresar letras en el código del producto {i+1}.")
                        print(f"   Debe ser un número entero. Intente de nuevo.")
                
                while True:
                    nombre = input(f"Ingrese el NOMBRE del producto {i+1}: ").strip()
                    if nombre:
                        break
                    print(f"✗ El nombre del producto {i+1} no puede estar vacío.")
                
                while True:
                    try:
                        precio = float(input(f"Ingrese el PRECIO del producto {i+1}: $"))
                        if precio > 0:
                            break
                        print(f"✗ El precio del producto {i+1} debe ser mayor a 0.")
                    except ValueError:
                        print(f"✗ Error: Precio inválido para el producto {i+1}. Debe ser un número.")
                
                while True:
                    try:
                        stock = int(input(f"Ingrese el STOCK del producto {i+1}: "))
                        if stock >= 0:
                            break
                        print(f"✗ El stock del producto {i+1} no puede ser negativo.")
                    except ValueError:
                        print(f"✗ Error: Stock inválido para el producto {i+1}. Debe ser un número entero.")
                
                inventario.agregar_producto(codigo, nombre, precio, stock)
                productos_agregados += 1
            
            print(f"\n{'='*50}")
            print(f"✓ Se agregaron {productos_agregados} producto(s) exitosamente")
            print(f"{'='*50}")
        
        case "2":
            print("\n--- BUSCAR PRODUCTO ---")
            while True:
                try:
                    codigo = int(input("Ingrese el código del producto: "))
                    producto = inventario.buscar_producto(codigo)
                    if producto:
                        print(f"\nProducto encontrado: {producto.mostrar_info()}")
                    else:
                        print("✗ Producto no encontrado")
                    break
                except ValueError:
                    print("✗ Código inválido. Debe ser un número entero. Intente de nuevo.")
        
        case "3":
            print("\n--- INVENTARIO COMPLETO ---")
            productos = inventario.listar_productos()
            if productos:
                for p in productos:
                    print(f"  {p.mostrar_info()}")
            else:
                print("El inventario está vacío")
        
        case "4":
            print("\n--- BUSCAR POR RANGO DE PRECIO ---")
            
            while True:
                try:
                    precio_min = float(input("Precio mínimo: $"))
                    if precio_min >= 0:
                        break
                    print("✗ El precio mínimo no puede ser negativo.")
                except ValueError:
                    print("✗ Precio inválido. Debe ser un número. Intente de nuevo.")
            
            while True:
                try:
                    precio_max = float(input("Precio máximo: $"))
                    if precio_max >= precio_min:
                        break
                    print(f"✗ El precio máximo debe ser mayor o igual a ${precio_min}")
                except ValueError:
                    print("✗ Precio inválido. Debe ser un número. Intente de nuevo.")
            
            productos = inventario.productos_por_precio(precio_min, precio_max)
            if productos:
                print(f"\nProductos entre ${precio_min} y ${precio_max}:")
                for p in productos:
                    print(f"  {p.mostrar_info()}")
            else:
                print("No se encontraron productos en ese rango")
        
        case "5":
            print("\n--- ACTUALIZAR STOCK ---")
            
            while True:
                try:
                    codigo = int(input("Código del producto: "))
                    break
                except ValueError:
                    print("✗ Código inválido. Debe ser un número entero. Intente de nuevo.")
            
            while True:
                try:
                    cantidad = int(input("Cantidad a sumar/restar (use - para restar): "))
                    break
                except ValueError:
                    print("✗ Cantidad inválida. Debe ser un número entero. Intente de nuevo.")
            
            inventario.actualizar_stock(codigo, cantidad)
        
        case "6":
            print("\n--- VISUALIZACIÓN DEL ÁRBOL (GRÁFICO) ---")
            inventario.visualizar_arbol_grafico()
        
        case "7":
            print("\n--- CARGAR PRODUCTOS DE PRUEBA ---")
            cargar_productos_prueba(inventario)
        
        case "8":
            print("\n¡Hasta luego!")
            break
        
        case _:
            print("✗ Opción inválida. Intente de nuevo.")
    
    input("\nPresione ENTER para continuar...")
