tabla = int(input("Ingrese el numero de la tabla que desea ver."))
print(f"Tabla # {tabla}")
for tabl in range(1, 11):
    resultado = tabla * tabl
    print(f"{tabla} x {tabl} = {resultado}")

contador = 1
print(f"Tabla # {tabla}")
while contador != 10:
    resultado = tabla * contador
    contador += 1
    print(f" {tabla} x {contador} = {resultado}")
