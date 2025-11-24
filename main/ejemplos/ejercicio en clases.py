continuar = "si"
while continuar == "si":
    sueldo = float(input("ingrese su sueldo: "))
    if sueldo < 500000:
        nuevo_sueldo = sueldo * 0.05
        sueldo += nuevo_sueldo
        print(
            f"Uste como es veneficiario tendra un aumento del 5%, y su nuevo sueldo es: {sueldo}$"
        )
    else:
        print("Usted no es veneficiario porque tienene un sueldo mayor a 500000$.")

    continuar = str(input("Desea continuar: (si)/(no): "))
    continuar = continuar.lower()
