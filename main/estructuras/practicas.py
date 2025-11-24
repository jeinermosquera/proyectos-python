
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def busqueda_binaria(numero, lista):
    bajo = 0
    alto = len(lista) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == numero:
            return True
        elif lista[medio] < numero:
            bajo = medio + 1
        else:
            alto = medio - 1
    return False


numero = int(input("Ingrese el numero que desea buscar en la lista: "))