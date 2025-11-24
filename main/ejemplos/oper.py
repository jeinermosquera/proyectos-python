num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
operacion = int(input("Ingrese la operación deseada: "))
match operacion:
    case 1:
        resultado = num1 + num2
    case 2:
        resultado = num1 - num2
    case 3:
        resultado = num1 * num2
    case 4:
        resultado = num1 / num2
    case _:
        resultado = "Operación no válida"

print("El resultado es:", resultado)
