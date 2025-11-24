saldo_inicial = 1000000

nuevo_saldo = 0
errores = 0
contador = 0
total_retirado = 0
while True:
    retiro = float(input(f"cuanto desea retirar en el retiro # {contador + 1}: "))
    contador += 1

    if retiro > saldo_inicial:
        print("No tienes saldo suficiente.")
        errores += 1
        if errores >= 3:
            print("cuenta bloquedad por intentos invalidos")
            break
        elif saldo_inicial == 0:
            print("saldo agotado.")
        else:
            continuar = int(
                input(f"Desea continuar, si(1), no(2), su saldo es {saldo_inicial}: ")
            )
            if continuar == 2:
                print("Sesion finalizada corretamente.")
                break

    else:
        saldo_inicial = saldo_inicial - retiro
        total_retirado += retiro

        seguir = int(
            input(f"desea continuar, si(1), no(2),su saldo es {saldo_inicial}: ")
        )
        if seguir == 2:
            print("Sesion finalizada corretamente.")
            break

print(40 * "=")
print(f"Su saldo retante es: {saldo_inicial}$")
print(f"el total rtirado fueron: {total_retirado}$")
print(f"El total de intentos fallidos fueron: {errores}")
