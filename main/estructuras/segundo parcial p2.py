lista = [5, 3, 8, 3, 2, 7, 5, 10, 1, 4]


def modificar_lista(lista):
    lista2 = lista.copy()

    lista2 = list(set(lista2))

    lista2.sort(reverse=True)

    lista2 = [i for i in lista2 if i % 2 == 0]
    # for i in lista2:
    #     if i % 2 != 0:
    #         lista2.remove(i)

    suma = sum(lista2)

    lista2.insert(0, suma)

    return lista2


print(f"Lista original: {lista}")
lista_modificada = modificar_lista(lista)
print(f"Lista modificada: {lista_modificada}")

print(lista_modificada[0] == sum(lista_modificada[1:]))
