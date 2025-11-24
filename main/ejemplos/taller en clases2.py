atendidos = 0
respiratorio = 0
gastrointestinal = 0
dermatologico = 0
otros = 0
total_edad = 0
while True:
    atendidos += 1
    nombre = str(input("\nIngrese su nombre completo: "))
    edad = int(input("Ingrese su edad: "))
    sintoma_principal = int(
        input(
            "Ingrese el numero de su sintoma principal: 1.(respiratorio), 2.(grastrointestinal), 3.(dermatologico), 4.(otros): "
        )
    )

    total_edad += edad

    if sintoma_principal == 1:
        respiratorio += 1
    elif sintoma_principal == 2:
        gastrointestinal += 1
    elif sintoma_principal == 3:
        dermatologico += 1
    elif sintoma_principal == 4:
        otros += 1

    continuar = int(
        input("Desea continuar, ingres el nuumero de lo que desea hacer, SI(1) NO(2): ")
    )
    if continuar == 2:
        break


promedio_edad = total_edad / atendidos
porcentaje_respiratorio = (respiratorio / atendidos) * 100

print(50 * "=")
if porcentaje_respiratorio >= 60:
    print(
        f"Alerta, {porcentaje_respiratorio}% de infectados, posible brote respiratorio."
    )

print(f"El total de pacientes atendidos fueron {atendidos}.")
print(f"El promedio de edad de los pacientes es {promedio_edad} años.")
print(f"la cantidad de pacientes por sintomas respiratorios son: {respiratorio}")
print(
    f"la cantidad de pacientes por sintomas gastrontestinales son: {gastrointestinal}"
)
print(f"la cantidad de pacientes por sintomas dermatologicos son: {dermatologico}")
print(f"la cantidad de pacientes por otros sintomas son: {otros}")
