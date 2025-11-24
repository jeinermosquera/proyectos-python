class CarritoCompra:
    def __init__(self, lista_productos=[]):
        self.lista_productos = lista_productos

    def agregar_producto(self, nombre, precio, cantidad):
        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        self.lista_productos.append(producto)

    def mostrar_carrito(self):
        for producto in self.lista_productos:
            print(
                f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}"
            )

    def total_compra(self):
        total = sum(
            producto["precio"] * producto["cantidad"]
            for producto in self.lista_productos
        )
        return total


carrito = CarritoCompra()

def tienda():
    while True:
        print("============ Carrito de Compra ============")
        print("1. Agregar producto")
        print("2. Mostrar carrito")
        print("3. Total de la compra")
        print("4. Salir")

        opcion = int(input("Ingrese una opcion: "))

        match opcion:
            case 1:
                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                carrito.agregar_producto(nombre, precio, cantidad)
            case 2:
                carrito.mostrar_carrito()
            case 3:
                total = carrito.total_compra()
                print(f"El total de la compra es: {total}")
            case 4:
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida, intente de nuevo.")

tienda()