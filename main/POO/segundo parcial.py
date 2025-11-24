class Rectangulo:
    def __init__(self, base=0, altura=0):
        self.base = base
        self.altura = altura
        return

    def area(self):
        self.resultado = self.base * self.altura
        return

    def perimetro(self):
        self.resultado = 2 * (self.base + self.altura)
        return


while True:
    print("==========Rectangulo=============")
    print("1.Area")
    print("2.Perimetro")
    print("3.salir")

    opcion = int(input("Elijs ls opcion que desea calcular: "))

    match opcion:

        case 1:
            base = float(input("ingrese la base del rectangulo: "))
            altura = float(input("ingrese la altura del rectangulo: "))
            rectangulo = Rectangulo(base, altura)
            rectangulo.area()
            print(f"el area del triangulo es {rectangulo.resultado}")

        case 2:
            base = float(input("ingrese la base del rectangulo: "))
            altura = float(input("ingrese la altura del rectangulo: "))
            rectangulo = Rectangulo(base, altura)
            rectangulo.perimetro()
            print(f"el area del triangulo es {rectangulo.resultado}")

        case 3:
            print("saliendo del programa.")
