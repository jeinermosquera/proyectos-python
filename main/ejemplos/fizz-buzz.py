"""
 Programa que me permite realizar el programa fizz buzz   
"""
# utilizamos un bucle desde 1 hasta 100
for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:# verificamos si el numero es multiplo de tres y de cinco
        print("Fizzbuzz")
    elif numero % 5 == 0: # aqui verificamos si el numero es multiplo de cinco
        print("Buzz")
    elif numero % 3 == 0: # aqui vemos si el numero es multiplo de tres
        print("Fizz")
    else:
        print(numero)
