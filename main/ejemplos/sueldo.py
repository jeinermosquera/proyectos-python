nombres = []
total_ventas = []
sueldo_fijo = 100000

numero_vendedores = int(input("Ingrese el número de vendedores: "))
for i in range(numero_vendedores):
    nombre = input(f"Ingrese el nombre del vendedor #{i + 1}: ")

    nombres.append(nombre)
    ventas = float(input(f"Ingrese el total de ventas del vendedor #{i + 1}: "))
    total_ventas.append(ventas)


for i in range(len(nombres)):
    sueldo_total = sueldo_fijo + total_ventas[i] * 0.15
    print(f"El sueldo total de {nombres[i]} es: {sueldo_total}")
