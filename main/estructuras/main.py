# son colecciones o conjuntos de datos o valores que permiten 
# almacenar múltiples elementos bajo un único nombre.

# años= list(range(2000, 2023))
# print(años)

numeros = [10, 20, 30, 40, 50, 7, 6, 8]

for numero in numeros:
    print(numero)

def recorrer_lista(numeros):
    lista = []
    for i in numeros:
        lista.append(i)
    return lista

def ordenar_lista(numeros):
    numeros.sort()
    return numeros


def longitud_lista(numeros):
    return len(numeros)

print("Lista original:")
print(recorrer_lista(numeros))

numeros = ordenar_lista(numeros)
print("Lista ordenada:")
print(numeros)

longitud = longitud_lista(numeros)
print("Longitud de la lista: " + str(longitud))