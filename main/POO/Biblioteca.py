class Biblioteca:
    def __init__(self, lista_libros=[]):
        self.lista_libros = lista_libros

    def agregar_libro(self, titulo, autor):
        if titulo not in self.lista_libros and autor not in self.lista_libros:
            self.lista_libros.append(titulo)
        else:
            print("El libro ya esta en la biblioteca.")

    def mostrar_libros(self):
        self.lista_libros.sort()
        for i in self.lista_libros:
            print(i)

    def buscar_libro(self, titulo):
        for i in self.lista_libros:
            if i == titulo:
                print("libro encontrado.")
                return
        print("Libro no encontrado.")


lista_libros = []
biblioteca = Biblioteca(lista_libros)

while True:
    print("============ Biblioteca ============")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Salir")

    opcion = int(input("Ingrese una opcion: "))

    match opcion:
        case 1:
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese el autor del libro: ")
            biblioteca.agregar_libro(titulo, autor)
        case 2:
            biblioteca.mostrar_libros()
        case 3:
            titulo = input("Ingrese el titulo del libro: ")
            biblioteca.buscar_libro(titulo)
        case 4:
            print("Saliendo...")
            break
        case _:
            print("Opcion no valida, intente de nuevo.")
