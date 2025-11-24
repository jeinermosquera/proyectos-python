def area():
    """Calcula área de N figuras geométricas"""
    print("\n=== EJERCICIO 12: Área de figuras ===")

    n = int(input("Número de figuras: "))

    for i in range(n):
        print(f"\nFigura {i+1}:")
        print("1 = Rectángulo")
        print("2 = Triángulo")
        codigo = int(input("Código de figura: "))

        if codigo == 1:
            base = float(input("Base del rectángulo: "))
            altura = float(input("Altura del rectángulo: "))
            area = base * altura
            print(f"Área del rectángulo: {area:.2f}")
        elif codigo == 2:
            base = float(input("Base del triángulo: "))
            altura = float(input("Altura del triángulo: "))
            area = (base * altura) / 2
            print(f"Área del triángulo: {area:.2f}")
        else:
            print("Código inválido")


area()
