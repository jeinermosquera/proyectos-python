class Persona:
    def __init__(self, nombre, edad, ID, sexo, altura, peso):
        self.nombre = nombre
        self.edad = edad
        self.ID = ID
        self.sexo = sexo
        self.altura = altura
        self.peso = peso

    def IMC(self):
        imc = self.peso / (self.altura**2)
        return imc

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"ID: {self.ID}")
        print(f"Sexo: {self.sexo}")
        print(f"Altura: {self.altura}")
        print(f"Peso: {self.peso}")


while True:
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    ID = input("Ingrese el ID de la persona: ")
    sexo = input("Ingrese el sexo de la persona (H/M): ")
    altura = float(input("Ingrese la altura de la persona en metros: "))
    peso = float(input("Ingrese el peso de la persona en kg: "))

    persona = Persona(nombre, edad, ID, sexo, altura, peso)

    print(f"El IMC de {persona.nombre} es: {persona.IMC():.2f}")
    if persona.es_mayor_de_edad():
        print(f"{persona.nombre} es mayor de edad.")
    else:
        print(f"{persona.nombre} es menor de edad.")

    persona.mostrar_datos()

    continuar = int(input("¿Desea ingresar otra persona? (s(1)/n(0)): "))
    if continuar != 1:
        break
