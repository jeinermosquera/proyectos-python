def viaje():
    """Calcula tiempo promedio de viaje de N carros"""
    print("\n=== EJERCICIO 22: Tiempo promedio de viaje ===")

    n = int(input("Número de carros: "))
    total_tiempo = 0

    for i in range(n):
        tiempo = int(input(f"Tiempo de viaje del carro {i+1} (minutos): "))
        total_tiempo += tiempo

    tiempo_promedio = total_tiempo / n
    print(f"Tiempo promedio de viaje: {tiempo_promedio:.2f} minutos")


viaje()
