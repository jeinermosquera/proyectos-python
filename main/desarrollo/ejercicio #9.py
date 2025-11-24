import math


def ecuacion():
    """Calcula Y según función por tramos de X"""
    print("\n=== EJERCICIO 9: Función por tramos ===")

    x = float(input("Ingrese el valor de X: "))
    p = math.pi  # Asumiendo que p es pi

    if x < 0:
        y = x * p
    elif x == 0:
        y = 1
    elif 0 < x < 100:
        y = x + x * p
    elif 100 <= x <= 200:
        y = 5.5 * x
    else:  # x > 200
        y = 10 * (x**2)

    print(f"Para X = {x}, Y = {y:.2f}")


ecuacion()
