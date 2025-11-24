class Producto:
    def __init__(self, nombre, precio, cantidad, codigo):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.codigo = codigo


class Supermercado:
    def __init__(self):
        self.lista = []

    def agregar(self, producto):
        self.lista.append(producto)

    def eliminar(self, codigo):
        for producto in self.lista:
            if producto.codigo == codigo:
                self.lista.remove(producto)
                print("Producto eliminado.")
                return
        print("Producto no encontrado.")

    def mostrar(self):
        return self.lista

    def vender(self, codigo):
        for producto in self.lista:
            if producto.codigo == codigo:
                if producto.cantidad > 0:
                    producto.cantidad -= 1
                    print("Venta realizada.")
                else:
                    print("No hay suficiente cantidad para vender.")
                return
        print("Producto no encontrado.")


# Crear instancia de supermercado
tienda = Supermercado()

while True:
    print(10 * " =", "Supermercado", 10 * " = ")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar productos")
    print("4. Vender producto")
    print("5. Salir")
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido para la opción.")
        continue

    match opcion:
        case 1:
            try:
                nombre = input("Ingrese el nombre del producto: ")
                if not nombre.isalpha():
                    raise ValueError("El nombre debe contener solo letras.")
                precio_str = input("Ingrese el precio del producto: ")
                if not precio_str.replace(".", "", 1).isdigit():
                    raise ValueError("El precio debe ser un número.")
                precio = float(precio_str)
                cantidad_str = input("Ingrese la cantidad del producto: ")
                if not cantidad_str.isdigit():
                    raise ValueError("La cantidad debe ser un número entero.")
                cantidad = int(cantidad_str)
                codigo = input("Ingrese el código del producto: ")
                if not nombre or not codigo:
                    raise ValueError("El nombre y el código no pueden estar vacíos.")
                if precio < 0 or cantidad < 0:
                    raise ValueError("El precio y la cantidad deben ser positivos.")
                producto = Producto(nombre, precio, cantidad, codigo)
                tienda.agregar(producto)
                print("Producto agregado correctamente.")
            except ValueError as ve:
                print(f"Error: {ve}")
            except Exception as e:
                print(f"Error inesperado: {e}")
        case 2:
            try:
                codigo = input("Ingrese el código del producto a eliminar: ")
                if not codigo:
                    raise ValueError("El código no puede estar vacío.")
                tienda.eliminar(codigo)
            except Exception as e:
                print(f"Error: {e}")
        case 3:
            try:
                productos = tienda.mostrar()
                if not productos:
                    print("No hay productos en el inventario.")
                else:
                    print("Productos en el inventario:")
                    for producto in productos:
                        print(
                            f"Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}, Código: {producto.codigo}"
                        )
            except Exception as e:
                print(f"Error al mostrar productos: {e}")
        case 4:
            try:
                codigo = input("Ingrese el código del producto a vender: ")
                if not codigo:
                    raise ValueError("El código no puede estar vacío.")
                tienda.vender(codigo)
            except Exception as e:
                print(f"Error: {e}")
        case 5:
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida, intente de nuevo.")
