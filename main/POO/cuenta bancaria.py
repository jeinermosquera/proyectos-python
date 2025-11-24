class Cuenta_bancaria:
    def __init__(self, numcuenta, titular, saldo=0):
        self.numero_cuenta = numcuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto < 0:
            print("No se puede depositar una cantidad negativa.")
        else:
            self.saldo += monto
            print("Se ha depositado correctamente.")

    def retirar(self, monto):
        if monto < 0:
            print("No se puede retirar una cantidad negativa.")
        elif monto > self.saldo:
            print("No se puede retirar esa cantidad de dinero por saldo insuficiente.")
        else:
            self.saldo -= monto
            print("Se ha retirado correctamente.")

    def mostrar_saldo(self):
        print(f"El saldo actual es: {self.saldo}")


print(" " * 20, "Cuenta bancaria")
numcuenta = int(input("Ingrese el número de cuenta: "))
titular = input("Ingrese el nombre del titular: ")
saldo = float(input("Ingrese el saldo inicial: "))

cuenta = Cuenta_bancaria(numcuenta, titular, saldo)

while True:
    print("\nSeleccione una opción:")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Mostrar saldo")
    print("4. Salir")
    opcion = int(input("Ingrese su opción: "))

    match opcion:
        case 1:
            num = int(input("Verifique el número de cuenta: "))
            tit = input("Verifique el titular: ")
            if num == cuenta.numero_cuenta and tit == cuenta.titular:
                monto = float(input("Ingrese el monto a depositar: "))
                cuenta.depositar(monto)
            else:
                print("Datos incorrectos. No se puede realizar el depósito.")
        case 2:
            num = int(input("Verifique el número de cuenta: "))
            tit = input("Verifique el titular: ")
            if num == cuenta.numero_cuenta and tit == cuenta.titular:
                monto = float(input("Ingrese el monto a retirar: "))
                cuenta.retirar(monto)
            else:
                print("Datos incorrectos. No se puede realizar el retiro.")
        case 3:
            cuenta.mostrar_saldo()
        case 4:
            print("Saliendo...")
            break
        case _:
            print("Opción inválida.")
