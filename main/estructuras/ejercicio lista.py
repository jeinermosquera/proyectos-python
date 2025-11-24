
# numeros = [3, 1, 4, -1, 5, -9, 2, -6, 5]
# numeros.sort()                                 # ordena los elementos de la lista en orden ascendente
# print(numeros)



# nombres = ["Ana", "Luis", "Carlos", "Luis", "Marta", "Luis", "Sofía"]

# nombres.sort()                                # ordena los elementos de la lista en orden alfabetico
# nombres.reverse()                             # invierte el orden de los elementos de la lista
# nombres.remove("Luis")                        # elimina la primera ocurrencia del elemento
# print(nombres.pop())                          # elimina y devuelve el ultimo elemento de la lista
# print(nombres.pop(1))                         # elimina un elemento en una  posicion especifica y devuelve el elemento eliminado
# nombres.insert(-6, "Elena")                   # inserta un elemento en la posicion especifica  de la lista
# indice = nombres.index("Carlos")              # devuelve el indice del elemento Carlos
# cantidad_Ana = nombres.count("Ana")           # cuenta cuantas veces aparece Ana en la lista
# indice_Carlos = nombres.index("Carlos")       # devuelve el indice del elemento Carlos
# nombres.extend(nombres)                       # concatena dos listas
# nombres.insert(2, "Elena")                    # inserta en la posicion 2 el elemento
# nombres.append("Pedro")                       # añade un elemento al final de la lista
# nombres.clear() 
# set(nombres)    elimina los duplicados        # elimina todos los elementos de la lista
numeros = [3, 1, 4, -1, 5, -9, 2, -6, 5]
print(numeros[1:5])                            # devuelve el numero de elementos de la lista
# numeros = list(set(numeros))  
# print(numeros)

# for i in numeros:
#     if i % 2 == 1:              # crea una copia de la lista
#         numeros.remove(i)   

# print(numeros)    # elimina los elementos impares de la lista

# for i in numeros:
#     print(i * 2)    

# for i in range(len(numeros)):
#     print(numeros[i] * 2)
# indice = 0
# while indice < len(numeros):
#     print(numeros[indice] * 2)
#     indice += 1