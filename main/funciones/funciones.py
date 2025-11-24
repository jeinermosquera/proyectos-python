#
variable = 6


def funcion():
    global variable
    variable = 10
    print(variable)  # Imprime 10


print(variable)  # Imprime 6
