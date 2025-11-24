class Tarjeta:
    def __init__(self, id, cantidad=0):
        self.id = id
        self.saldo = cantidad
        return

    def mostrar_saldo(self):
        print(f"El saldo es {self.saldo} $")
        return


t = Tarjeta("11111111", 10000)
t.mostrar_saldo()
