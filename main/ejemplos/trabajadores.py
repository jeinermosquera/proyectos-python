total_trabajadores = int(input("ingrese el numero total de trabajadores: "))

nombres = []
sueldos = []

for trabajador in range(total_trabajadores):
    nombre = str(input(f"Ingrese el nombre de tranbjador # {trabajador + 1}: "))
    sueldo = float(input(f"Ingrese el sueldo del trabajador # {trabajador + 1}: "))
    if sueldo < 265000:
        sueldo += sueldo * 0.1
    elif sueldo >= 265000 and sueldo <= 450000:
        sueldo += sueldo * 0.08
    elif sueldo >= 450000:
        sueldo += sueldo * 0.05
    nombres.append(nombre)
    sueldos.append(sueldo)

for trabajadores in range(total_trabajadores):
    print(f"{nombres[trabajadores]} su nuevo sueldo es: {sueldos[trabajadores]}$")
