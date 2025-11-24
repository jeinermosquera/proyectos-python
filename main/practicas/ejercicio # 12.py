# algoritmo de busqueda ordenada
def busqueda_binaria(lista, objetivo):
    bajo = 0
    alto = len(lista) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1


lista = []
for i in range(1, 10):
    lista.append(i)

objetivo = int(input("Ingrese el número del 1 al 100 que desea buscar: "))
resultado = busqueda_binaria(lista, objetivo)

if resultado != -1:
    print(f"Elemento encontrado en la posición: {resultado}")
else:
    print("Elemento no encontrado.")
