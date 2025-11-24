
# ejemplo de lista original
lista = [5, 3, 8, 3, 2, 7, 5, 10, 1, 4]

def modificar_lista(lista):
    # crear una copia para no modificar la lista original
    lista2 = lista.copy()
    # eliminar duplicados convirtiendo a set y volver a lista (el orden se pierde aquí)
    lista2 = list(set(lista2))
    # ordenar en orden descendente (mayor a menor)
    lista2.sort(reverse=True)

    # filtrar solo los números pares (de la lista única y ordenada)
    lista2 = [i for i in lista2 if i % 2 == 0]

    # sumar todos los elementos pares obtenidos
    suma = sum(lista2)
    # insertar la suma al inicio de la lista (posición 0)
    lista2.insert(0, suma)

    # devolver la lista modificada
    return lista2

print(f"Lista original: {lista}")
lista_modificada = modificar_lista(lista)
print(f"Lista modificada: {lista_modificada}")

# comprobar que el primer elemento (la suma) coincide con la suma del resto
print(lista_modificada[0] == sum(lista_modificada[1:]))