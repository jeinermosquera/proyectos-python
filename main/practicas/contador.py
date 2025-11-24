palabra = str(input("Ingrese una palabra: "))
palabra = palabra.lower()

contador = 0
for letra in palabra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador += 1

print("Las vocales aparecen", contador, "veces en la palabra.")
