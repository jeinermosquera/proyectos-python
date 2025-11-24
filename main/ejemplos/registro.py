edades = []
pesos = []
estaturas = []
generos = []
while True:
    edad = str(input("\nIngrese su nombre:"))
    peso = int(input("Ingrese su peso en kg por favor:"))
    estatura = float(input("Ingrese su estatura en centimetros por favor: "))
    genero = int(input("Ingrese su genero. (1)hombre, (2)mujer: "))

    edades.append(edad)
    pesos.append(peso)
    estaturas.append(estatura)
    generos.append(genero)

    continuar = int(input("Desea continuar, 1.(si) 2.(no): "))
    if continuar == 1:
        break
for eda, pes, estatur, gener in zip(edades, pesos, estaturas, generos):

    edad_promedio += eda
    peso_promedio += pes
    estatura_promedio += estatur
    genero_promedio += gener
