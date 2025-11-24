import os


class Calculadora:
    def __init__(self, numero1, numero2):
        self.num1 = numero1
        self.num2 = numero2

    def sumar(self):
        self.resultado = self.num1 + self.num2
        return

    def restar(self):
        self.resultado = self.num1 - self.num2
        return

    def multiplicar(self):
        self.resultado = self.num1 * self.num2
        return

    def dividir(self):
        if self.num2 != 0:
            self.resultado = self.num1 / self.num2
        else:
            self.resultado = "Error: Division por cero"
        return


while True:

    print("\n=== Calculadora ===")
    print("\n1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    try:
        opcion = int(input("Elige una opcion: "))
        if opcion < 1 or opcion > 6:
            raise ValueError
        else:
            try:
                numero1 = float(input("Ingresa el primer numero: "))
                numero2 = float(input("Ingresa el segundo numero: "))
            except ValueError:
                print("Por favor, ingresa un numero valido.")
                continue
    except ValueError:
        print("Por favor, ingresa un numero valido.")
        continue

    print(40 * "=")

    calculo = Calculadora(numero1, numero2)

    match opcion:
        case 1:
            calculo.sumar()
            print("El resultado de la suma es:", calculo.resultado)
        case 2:
            calculo.restar()
            print("El resultado de la resta es:", calculo.resultado)
        case 3:
            calculo.multiplicar()
            print("El resultado de la multiplicacion es:", calculo.resultado)
        case 4:
            calculo.dividir()
            print("El resultado de la division es:", calculo.resultado)

        case 5:
            print("Saliendo...")
            break
