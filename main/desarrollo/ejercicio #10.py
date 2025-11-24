import math


def primo(numero):
    """Verifica si un número es primo"""
    if numero < 2:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True


def verificacion():
    """Verifica si N números son primos"""
    print("\n=== EJERCICIO 10: Números primos ===")

    n = int(input("Cantidad de números a evaluar: "))

    for i in range(n):
        numero = int(input(f"Número {i+1}: "))

        if primo(numero):
            print(f"{numero} es primo")
        else:
            print(f"{numero} no es primo")


verificacion()
