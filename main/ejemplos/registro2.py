nombres = []
edades = []
pesos = []
estaturas = []
sexos = []

while True:
    nombre = input("Ingrese el nombre del estudiante (o '2' para terminar): ")
    if nombre == "2":
        break
    nombres.append(nombre)
    edad = int(input("Ingrese la edad del estudiante: "))
    edades.append(edad)
    peso = float(input("Ingrese el peso del estudiante: "))
    pesos.append(peso)
    estatura = float(input("Ingrese la estatura del estudiante: "))
    estaturas.append(estatura)
    sexo = int(input("Ingrese el sexo del estudiante ((1)Masculino/(2)Femenino): "))
    sexos.append(sexo)

cantidad_mujeres = 0
cantidad_hombres = 0
edad_Mujeres = 0
edad_Hombres = 0
peso_Mujeres = 0
peso_Hombres = 0
estatura_Mujeres = 0
estatura_Hombres = 0
for i in range(len(sexos)):
    if sexos[i] == 1:
        cantidad_mujeres += 1
        edad_Mujeres += edades[i]
        peso_Mujeres += pesos[i]
        estatura_Mujeres += estaturas[i]
    elif sexos[i] == 2:
        cantidad_hombres += 1
        edad_Hombres += edades[i]
        peso_Hombres += pesos[i]
        estatura_Hombres += estaturas[i]

print("Cantidad de mujeres:", cantidad_mujeres)
print("Cantidad de hombres:", cantidad_hombres)
print(
    f"Edad promedio mujeres:",
    {edad_Mujeres / cantidad_mujeres if cantidad_mujeres > 0 else 0},
)
print(
    f"Edad promedio hombres:",
    {edad_Hombres / cantidad_hombres if cantidad_hombres > 0 else 0},
)
print(
    f"Peso promedio mujeres:",
    {peso_Mujeres / cantidad_mujeres if cantidad_mujeres > 0 else 0},
)
print(
    f"Peso promedio hombres:",
    {peso_Hombres / cantidad_hombres if cantidad_hombres > 0 else 0},
)
print(
    f"Estatura promedio mujeres:",
    {estatura_Mujeres / cantidad_mujeres if cantidad_mujeres > 0 else 0},
)
print(
    f"Estatura promedio hombres:",
    {estatura_Hombres / cantidad_hombres if cantidad_hombres > 0 else 0},
)
