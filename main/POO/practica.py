# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def datos(self):
#         print(f"El nombre es {self.nombre}")
#         print(f"La edad es {self.edad}")
#         return


# nombre = str(input("Ingrese su nombre por favor: "))
# edad = int(input("ingrese su edad por favor: "))
# persona = Persona(nombre, edad)
# persona.datos()


# class Coche:
#     def __init__(self, marca, modelo, color):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color

#     def datos(self):
#         print(f"La marca: {self.marca}")
#         print(f"El modelo: {self.modelo}")
#         print(f"El color: {self.color}")
#         return

#     def arrancar(self):
#         print("El coche arranco")
#         return

#     def detener(self):
#         print("El coche se detuvo")
#         return


# marca = str(input("Ingrese la marca del coche: "))
# modelo = str(input("Ingrese el modelo del coche: "))
# color = str(input("Ingrese el color del coche: "))
# coche = Coche(marca, modelo, color)
# coche.datos()
# coche.arrancar()
# coche.detener()


class Estudiante:
    def __init__(self, nombre, edad, notas=[]):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def agregar_nota(self, nota):
        self.notas.append(nota)
        return

    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0
        else:
            return sum(self.notas) / len(self.notas)

    def aprobo(self):
        promedio = self.calcular_promedio()
        if promedio >= 3.0:
            return True
        else:
            return False


nombre_estudiante = input("Ingrese el nombre del estudiante: ")
edad_estudiante = int(input("Ingrese la edad del estudiante: "))
estudiante1 = Estudiante(nombre_estudiante, edad_estudiante)
for i in range(3):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    nota.append(nota)
    estudiante1.agregar_nota(nota)
