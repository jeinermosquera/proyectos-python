"""
Programa que me permite mostrar todas la poera iones basicas
a prtir de dos numerosinfresado por el usario.

"""

# Validamos la entrada para que solamente ingrese numeros

while True:
    """
    utilizamos el try - except para capturar
    po+
    sibles errores del usuario.

    """
    try:
        numero1 = int(input("\nIngrese el primer numero: "))
        break
    except ValueError:
        print("Por favor ingresa numeros no letras ni simbolos, intetalo de nuevo.")
# Validamos la entrada para que solamente ingrese numeros
while True:
    """
    utilizamos el try - except para capturar
    posibles errores del usuario.
    """
    try:
        numero2 = int(input("Ingrese el segundo numero: "))
        break
    except ValueError:
        print("Por favor ingresa numeros no letras ni simbolos, intetalo de nuevo.")


# Hacemos la operaciones correspondientes y mostramos el resultado al usuario
print(f"La suma: {numero1} + {numero2} = {numero1 + numero2}")
print(f"Resta: {numero1} - {numero2} = {numero1 - numero2}")
print(f"Multiplicacion: {numero1 } x {numero2} = {numero1 * numero2}")
"""
verificamos si el segundo numero es 0 y le mandamos un mensaje
al usuario que no se puede hacer la multiplicacion por cero.

"""
try:
    print(f"Division: {numero1} / {numero2} = {numero1 / numero2}")
except ZeroDivisionError:
    print("No es posible hacer una division por cero.")
