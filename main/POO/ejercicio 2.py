class Calculo_geometrico:
    def __init__(self, altura=0, base=0, lado1=0, lado2=0, radio=0, lado3=0):
        self.altura = altura
        self.base = base
        self.lado1 = lado1
        self.lado2 = lado2
        self.radio = radio
        self.lado3 = lado3
        return

    def area_triangulo(self):
        self.resultado = (self.altura * self.base) / 2
        return

    def perimetro_triangulo(self):
        self.resultado = self.lado1 + self.lado2 + self.lado3
        return

    def area_circulo(self):
        self.resultado = 3.14159 * (self.radio**2)
        return

    def circunferencia_circulo(self):
        self.resultado = 2 * 3.14159 * self.radio
        return

    def area_rectangulo(self):
        self.resultado = self.altura * self.base
        return

    def perimetro_rectangulo(self):
        self.resultado = 2 * (self.altura + self.base)
        return


while True:
    print("============ Calculo ============")
    print("\n1. Area rectangulo")
    print("2. perimetro triangulo")
    print("3. Area circulo")
    print("4. perimetro rectangulo")
    print("5. perimetro triangulo")
    print("6. circunferencia circulo")
    print("7. Salir")

    opcion = int(input("\nEliga una opcion por favor: "))

    match opcion:

        case 1:
            altura = float(input("\nIngresa la altura del rectangulo: "))
            base = float(input("Ingresa la base del rectangulo: "))
            calculo = Calculo_geometrico(altura, base)
            calculo.area_rectangulo()
            print(f"El area del rectangulo es:{calculo.resultado}")

        case 2:
            altura = float(input("\nIngresa la altura del triangulo: "))
            base = float(input("Ingresa la base del triangulo: "))
            lado1 = float(input("Ingresa el lado 1 del triangulo: "))
            lado2 = float(input("Ingresa el lado 2 del triangulo: "))
            lado3 = float(input("Ingresa el lado 3 del triangulo: "))
            calculo = Calculo_geometrico(altura, base, lado1, lado2, lado3)
            calculo.perimetro_triangulo()
            print("El perimetro del triangulo es:", calculo.resultado)

        case 3:
            radio = float(input("\nIngresa el radio del circulo: "))
            calculo = Calculo_geometrico(radio=radio)
            calculo.area_circulo()
            print("El area del circulo es:", calculo.resultado)

        case 4:
            altura = float(input("\nIngresa la altura del rectangulo: "))
            base = float(input("Ingresa la base del rectangulo: "))
            calculo = Calculo_geometrico(altura, base)
            calculo.perimetro_rectangulo()
            print("El perimetro del rectangulo es:", calculo.resultado)

        case 5:
            lado1 = float(input("\nIngresa el lado 1 del triangulo: "))
            lado2 = float(input("Ingresa el lado 2 del triangulo: "))
            lado3 = float(input("Ingresa el lado 3 del triangulo: "))
            calculo = Calculo_geometrico(lado1, lado2, lado3)
            calculo.perimetro_triangulo()
            print("El perimetro del triangulo es:", calculo.resultado)

        case 6:
            radio = float(input("\nIngresa el radio del circulo: "))
            calculo = Calculo_geometrico(radio=radio)
            calculo.circunferencia_circulo()
            print("La circunferencia del circulo es:", calculo.resultado)

        case 7:
            print("Saliendo...")
            break

        case _:
            print("Opcion no valida, ingrese un numero del 1 al 7, intente de nuevo.")
