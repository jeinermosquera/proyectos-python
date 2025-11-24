class Empleado:
    def __init__(self, nombre, saldo_base):
        self.nombre = nombre
        self.saldo_base = saldo_base

    def calcular_saldo(self):
        print(f"Sueldo: {self.saldo_base}")
        return


class EmpleadoComisionado(Empleado):
    def __init__(self, nombre, saldo_base, ventas, comision):
        super().__init__(nombre, saldo_base)
        self.ventas = ventas
        self.comision = comision

    def calcular_sueldo(self):
        sueldo_base = self.ventas * self.comision
        print(f"Sueldo comisionado: {sueldo_base}")
        return


nombre = input("Ingrese el nombre del empleado: ")
saldo_base = float(input("Ingrese el saldo base del empleado: "))
tipo_empleado = int(input("Ingrese el tipo de empleado (comisionado(1)/normal(2)): "))

if tipo_empleado == 1:
    ventas = float(input("Ingrese el total de ventas: "))
    comision = float(input("Ingrese el porcentaje de comision: "))
    empleado = EmpleadoComisionado(nombre, saldo_base, ventas, comision)
else:
    empleado = Empleado(nombre, saldo_base)

empleado.calcular_sueldo()
