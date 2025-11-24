class Factura:
    def __init__(
        self, nombre_producto, codigo_producto, cantida_producto, precio_producto
    ):
        self.nombre_producto = nombre_producto
        self.codigo_producto = codigo_producto
        self.cantida_producto = cantida_producto
        self.precio_producto = precio_producto
        return

    def monto_factura(self):
        self.resultado = self.cantida_producto * self.precio_producto
        return


print(40 * " ", "FACTURA")
nombre_producto = str(input("Ingrese el nombre del producto: "))
codigo_producto = int(input("ingrese el codigo de productos: "))
cantida_producto = float(input("ingrese la cantidad de productos: "))
if cantida_producto < 0:
    cantida_producto = 0

precio_producto = float(input("ingrese el precio del producto: "))
if precio_producto < 0:
    precio_producto = 0

factura = Factura(nombre_producto, codigo_producto, cantida_producto, precio_producto)
factura.monto_factura()
print(f"el resultado de la factura es: {factura.resultado} $")
