# from getpass import getpass
# def login():
#     username = input("Ingrese su nombre de usuario: ")
#     password = getpass("Ingrese su contraseña: ")
#     if username == "admin" and password == "1234":
#         print("Inicio de sesión exitoso.")  
#     else:
#         print("Nombre de usuario o contraseña incorrectos.")
#         login() 

# login()
# a = [1, 2, 3, 4, 5]
# a[1:3] = []
# print(a)

# def  numeros_pares(numeros):
#     for i in numeros:
#         if i % 2 == 0:
#             print(i)
#         else:
#             continue

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# numeros_pares(numeros)
# def suma(numeros):
#     suma = sum(numeros)
#     print(f"la suma de todos los numeros es: {suma}")
#     return

# def promedio(numeros):
#     promedio = sum(numeros) / len(numeros)
#     print(f"el promedio es: {promedio}")

# print("ingrse 5 numeros por favor.")
# numeros = []
# for i in range(5):
#     numero = int(input(f"ingrse el numero  # {i+1}:"))
#     numeros.append(numero)

# suma(numeros)
# promedio(numeros)


# def eliminar_duplicados(numeros):
#     numeros = list(set(numeros))
#     print(numeros)
#     return


# eliminar_duplicados(numeros)

# numeros = [3, 1, 4, -1, 5, -9, 2, -6, 5, 3, 4, 2, -1]

# def mayor_menor(numeros):
#     menor = 0
#     mayor = 0
#     for i in numeros:
#         if i > mayor:
#             mayor = i
#         elif i < menor:
#             menor = i
#     print(f"el mayor es: {mayor}")
#     print(f"el menor es: {menor}")

# mayor_menor(numeros)

# Clase Estudiante

# Crea una clase Estudiante con:

# Atributos: nombre, edad, notas (lista)

# Métodos:

# promedio() → devuelve el promedio de las notas

# mostrar_info() → imprime los datos del estudiante

class estudiante():
    def __init__(self,nombre, edad,notas =[]):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas
    
    def promedio(self):
        promedio = sum(self.notas) /len(self.notas)
        return promedio

    def mostrar_informacion(self):
        print("informacion")
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        print(f"notas: {self.notas}")
        print(f"promedio:{self.promedio()}")

nombre = input("ingrese su nombre por favor:")
edad = float(input("ingrese su edad por favor: "))
notas = []
for i in range(3):
    nota = float(input(f"ingrese la nota {i+1}: "))
    notas.append(nota)

estudiante = estudiante(nombre, edad, notas)
estudiante.mostrar_informacion()
