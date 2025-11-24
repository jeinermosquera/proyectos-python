numeros = int(input("ingrese el numero de carros por favor: "))

tiempo_total = 0
for numero in range(numeros):
    tiempo = int(
        input(f"Ingrese el numero de munutos que se demoro el carro {numero + 1}: ")
    )
    tiempo_total += tiempo
tiempo_promedio = tiempo_total / numeros
print(
    f"El tiempo recorrido promedio de recorrido entre las dos ciudades es de:{tiempo_promedio} minutos."
)
