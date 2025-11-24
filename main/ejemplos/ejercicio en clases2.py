trabajadores = int(input("Ingrese el numero de trabajadores: "))

for trabajador in range(trabajadores):
    sueldo1 = float(input(f"ingrese el sueldo del trabajador {trabajador + 1} : "))

    nuevo_sueldo = sueldo1 * 0.06
    sueldo1 += nuevo_sueldo
    if sueldo1 < 380000:
        incremento = sueldo1 * 0.1
        sueldo2 = sueldo1 + incremento
        print(
            f"Su primer aumento es del 6%  en su sueldo y su sueldo quedaen {sueldo1}$ y ademas tendra otro aumento del 10%, y su sueldo final es: {sueldo2}$"
        )
    else:
        print(
            f"Usted no es veneficiario del segundo aumento porque tienene un sueldo mayor a 380000$ y su sueldo es de {sueldo1}$."
        )
