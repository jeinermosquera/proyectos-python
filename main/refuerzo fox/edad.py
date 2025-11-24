total_cuenta = float(input("Ingrese el total de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina: "))
propina = (total_cuenta * porcentaje_propina) / 100

total_por_personas = int(input("Ingrese el numero de persona para dividir la cuenta: "))

total_con_propina = total_cuenta + propina
total_por_personas = total_con_propina / total_por_personas
total_por_personas = round(total_por_personas, 2)
print(f"El total por persona es: {total_por_personas} $")
