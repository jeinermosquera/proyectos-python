listas = []

def agregar_numero(numero):
    listas.append(numero)
    print("numero añadido con exito.")
    return

def agregar_por_posicion(numero,posicion):
    print("numero insetado con exito.")
    listas.insert(posicion,numero)
    return

def longitud(listas):
    longitud = len(listas)
    print(f"la longitud es: {longitud}")
    return

def eliminar_ultimo(listas):
    listas.pop
    print("el numero fue eliminado con exito.")

def eliminar_posiscion(listas,posicion):
    if posicion < 0 or posicion > len(listas):
        print("indice fuera del rango.")
    else:
        listas.pop(posicion)
        print("el numero fue eliminado con exito.")
    return

def contar_numero(listas,numero):
    cantidad = listas.count(numero)
    print(f"el numero {numero} se encuentra {cantidad} veces en la lista.")
    return


def posicion_numero(listas,numero):
    if numero in listas:
        indice = listas.index(numero)
        print(f"el numero {numero} se encuentra en la posicion {indice}.")
    else:
        print(f"el numero {numero} no se encuentra en la lista.")
    return

def mostrar_numeros(listas):
    print("los numeros en la lista son:")
    for i in listas:
        print(i)
    return

def menu():
    while True:
        print("====Menu de opciones====")
        print("1. Agregar numero")
        print("2. Agregar numero por posicion")
        print("3. Mostrar longitud de la lista")
        print("4. Eliminar ultimo numero")
        print("5. Eliminar numero por posicion")
        print("6. Contar la cantidad de un numero")
        print("7. Mostrar posicion de un numero")
        print("8. Mostrar todos los numeros")
        print("9. Salir")
        opcion = int(input("ingrese una opcion: "))
    
    
        if opcion == 1:
            numero = int(input("ingrese el numero a agregar: "))
            agregar_numero(numero)
        elif opcion == 2:
            numero = int(input("ingrese el numero a agregar: "))
            posicion = int(input("ingrese la posicion donde desea agregar el numero: "))
            agregar_por_posicion(numero,posicion)
        elif opcion == 3:
            longitud(listas)
        elif opcion == 4:
            eliminar_ultimo(listas)
        elif opcion == 5:
            posicion = int(input("ingrese la posicion del numero a eliminar debe ser desde 1: "))
            eliminar_posiscion(listas,posicion)
        elif opcion == 6:
            numero = int(input("ingrese el numero a contar: "))
            contar_numero(listas,numero)
        elif opcion == 7:
            numero = int(input("ingrese el numero a buscar: "))
            posicion_numero(listas,numero)
        elif opcion == 8:
            mostrar_numeros(listas)
        elif opcion == 9:
            print("saliendo del programa.")
            break
        else:
            print("opcion no valida, por favor intente de nuevo.")
        
menu()