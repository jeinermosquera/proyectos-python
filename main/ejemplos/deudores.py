# nombres = ["Juan", "Ana", "Luis", "Maria"]
# edades = [25, 30, 22, 28]
# generos = ["hombre", "mujer", "hombre", "mujer"]

# for nombre, edad, genero in zip(nombres, edades, generos):
#     print(f"Hola, {nombre}! Tienes {edad} años y eres {genero}.")

# lista = [1, 2, 4, 7, 4]

# for i in range(len(lista)):
#     elemento = lista[i]
#     if type(elemento) == int:
#         lista[i] = elemento + 4
#         print(lista[i])

# for i in range(1, 10):
#     for j in range(i):
#         print(i, end=" ")
#     print()
# n = 6
# a, b = 0, 1
# print(a, b)
# for i in range(2, n):
#     c = a + b
#     print(c)
#     a = b
#     b = c

# def fibonacci(n):
#     serie = [0, 1]
#     a, b = 0, 1
#     for i in range(2, n):
#         siguiente = a + b
#         serie.append(siguiente)
#         a = b
#         b = siguiente
#     return serie
