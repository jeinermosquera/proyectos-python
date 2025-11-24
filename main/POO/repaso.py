class Usuario:
    def __init__(self, nombre, apellido, correo, contraseña, premium):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = contraseña
        self.premium = premium
        return

    def iniciar_sesion(self, usu, contra):
        if usu == self.correo and contra == self.contraseña:
            print("Iniciando sesión...")
            return
        else:
            print("usuario o contraseña incorrecta.")
            return

    def cerrar_sesion(self):
        print("Cerrando sesión...")
        return

    def editar_perfil(self):
        print("Editando perfil...")
        return

    def cambiar_contraseña(self):
        print("Su contraseña fue cambiada con exito.")
        return

    def pasar_a_premium(self):
        print("Pasando a premium...")
        return

    def publicar_en_comunidad(self):
        print("Publicando en comunidad...")
        return


nombre = str(input("Ingrese su nombre por favor: "))
apellido = str(input("Ingrese su apellido por favor: "))
correo = str(input("Ingrese su correo por favor: "))
contraseña = str(input("ingrese su contraseña por favor: "))
premium = int(input("El usuario es premium si (1)/ no (2): "))

usuario = Usuario(nombre, apellido, correo, contraseña, premium)


while True:
    print("==============usuario==============")
    print("1. Iniciar sesion")
    print("2. Cerrar sesion")
    print("3. Editar perfil")
    print("4. Cambiar contraseña")
    print("5. Pasar a premium")
    print("6. Salir")

    opcion = int(input("Ingrese una opcion: "))

    match opcion:
        case 1:
            Usu = str(input("ingrese su usuario: "))
            contra = str(input("ingrese su contraseña: "))
            usuario.iniciar_sesion(Usu, contra)

        case 2:
            usuario.cerrar_sesion()

        case 3:
            nombre = str(input("Ingrese su nombre: "))
            apellido = str(input("Ingrese s nombre: "))
            usuario.editar_perfil()

        case 4:
            contraseña = str(input("Ingrese su nueva contraseña: "))
            usuario.cambiar_contraseña()

        case 5:
            premium = int(input("El usuario es premium si(1)no(2)"))
            if premium == 1:
                print("No  es necesario cambiarse a premium porque ya lo eres.")
            else:
                print("El usuaerio ya es premium")

        case 6:
            print("Has salido con exito del programa")
            break
