tabla = int(input("Ingrese el numero de la tabla que desea ver: "))

contador = 1
print(f"Tabla # {tabla}")
while contador != 10:
    resultado = tabla * contador
    contador += 1
    print(f" {tabla} x {contador} = {resultado}")
