nuevo_sueldo = 0
while True:
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    if sueldo < 500000:
        nuevo_sueldo = sueldo * 0.05
        print(
            f"su sueldo anterior era {sueldo} y el nuevo sueldo es de: {nuevo_sueldo} $"
        )
    else:
        print(f"El su sueldo es de {sueldo} y no tiene derecho a un aumento.")

    continuar = int(input("¿Desea ingresar otro sueldo? s(1)/n(2): "))
    if continuar == 2:
        break
