import math

a = int(input("ingres el valor de a: "))

b = int(input("ingrese el valor de b: "))

c = int(input("ingrese el valor de c: "))

if a != 0 and b != 0 and c != 0:
    raiz = ((b**2) - (4 * a * c)) ** (0.5)

    if raiz > 0:
        x1 = (-b + raiz) / (2 * a)
        x2 = (-b - raiz) / (2 * a)
        print(f" x1 es igual a: {x1}")
        print(f" x2 es igual a: {x2}")

    else:
        x1 = (-b + raiz) / (2 * a)
        print(f" x1 es igual a: {x1}")
