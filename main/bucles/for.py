tabla = int(input("Ingrese el numero de la tabla que desea ver: "))
print(f"Tabla # {tabla}")
for tabl in range(1, 11):
    resultado = tabla * tabl
    print(f"{tabla} x {tabl} = {resultado}")
