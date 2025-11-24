class Cuenta_bancaria():
    def __init__(self,titular,saldo,numero_cuenta,contrseña):
        self.titular = titular
        self.saldo = saldo
        self.numero_cuenta = numero_cuenta
        self.contrseña = contrseña

    def crear_cuenta(self):
        pass

        print(f"Cuenta creada para {self.titular} con un saldo inicial de {self.saldo}.")

    def depositar(self, monto):
        if monto < 0:
            print("No puedes depositar un saldo negativo. Intenta nuevamente.")
        else:
            self.saldo += monto
            print("Saldo depositado con exito.")

    def retirar(self,monto):
        if monto > self.saldo:
            print("Saldo insuficiente, intenta nuevamente.")
        elif monto < 0:
            print("No puedes retirar un saldo negativo, intenta nuevamente.")
        else:
            self.saldo -= monto
            print("Retiro realizado con exito.")

    def consultar_saldo(self):
        print(f"El saldo actual es: {self.saldo}")

def info_cuenta():
    while True:
        print("~" * 50)
        print(" " * 20, "Cuenta bancaria")
        print("1. Crear cuenta")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Consultar saldo")
        print("5. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        match opcion:
            case 1:
                titular = input("Ingrese el nombre del titular de la cuenta: ")
                while True:
                    try:
                        numero_cuenta = int(input("Ingrese el número de cuenta: "))
                        break
                    except ValueError:
                        print("Por favor, ingrese un número de cuenta válido.")
                while True:
                    try:
                        saldo = float(input("Ingrese el saldo inicial de la cuenta: "))
                        break
                    except ValueError:
                        print("Por favor, ingrese un valor numérico válido para el saldo.")
                contraseña = input("Cree una contraseña para la cuenta: ")
                cuenta = Cuenta_bancaria(titular, saldo, numero_cuenta, contraseña)
                cuenta.crear_cuenta()
            case 2:
                if 'cuenta' in locals():
                    cuenta = Cuenta_bancaria(titular, saldo, numero_cuenta, contraseña)
                    while True:
                        numero_cuenta = int(input("Ingrese su número de cuenta: "))
                        while True:
                            try:
                                if numero_cuenta != cuenta.numero_cuenta:
                                    print("Número de cuenta incorrecto. Intente nuevamente.")
                                    numero_cuenta = int(input("Ingrese su número de cuenta: "))
                                else:
                                    break
                            except ValueError:
                                print("Por favor, ingrese un número de cuenta válido.")
                        contraseña = input("Ingrese su contraseña: ")
                        if contraseña != cuenta.contraseña:
                            print("Contraseña incorrecta. Intente nuevamente.")
                        else:
                            cuenta.depositar(monto)
                            break
                        

                    while True:
                        try:
                            monto = float(input("Ingrese el monto a depositar: "))
                            break
                        except ValueError:
                            print("Por favor, ingrese un valor numérico válido para el monto.")
                    cuenta.depositar(monto)
                else:
                    print("Primero debes crear una cuenta.")
            case 3:
                if 'cuenta' in locals():
                    while True:
                        try:
                            monto = float(input("Ingrese el monto a retirar: "))
                            break
                        except ValueError:
                            print("Por favor, ingrese un valor numérico válido para el monto.")
                    cuenta.retirar(monto)
                else:
                    print("Primero debes crear una cuenta.")
            case 4:
                if 'cuenta' in locals():
                    cuenta.consultar_saldo()
                else:
                    print("Primero debes crear una cuenta.")
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Opción no válida.")

info_cuenta()