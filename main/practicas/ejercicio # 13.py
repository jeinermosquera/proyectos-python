nombres = []
edades = []
generos = []
while True:
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    genero = input("Introduce tu género: ")
    salir = int(input("¿Deseas salir? (si(1)/no (0)): "))
    salir

    nombres.append(nombre)
    edades.append(edad)
    generos.append(genero)

    if salir == 1:
        break
for nombre, edad, genero in zip(nombres, edades, generos):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Género: {genero}")


